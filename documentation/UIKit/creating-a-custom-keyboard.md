# Creating a custom keyboard

**Framework**: UIKit

Add an extension to your Xcode project to provide systemwide customized text input.

#### Overview

A custom keyboard replaces the system keyboard for users who want capabilities such as a novel text input method or the ability to enter text in a language not otherwise supported. Users enable your custom keyboard in Settings, which allows them to access your keyboard systemwide wherever third-party keyboards are supported.

> **Note**:  If your keyboard is specific to your app, use a [`UIInputView`](uiinputview.md) instead of creating a custom keyboard. Set the [`inputView`](uitextfield/inputview.md) property of text fields or text views to a view that should replace the system keyboard.

 If your keyboard is specific to your app, use a [`UIInputView`](uiinputview.md) instead of creating a custom keyboard. Set the [`inputView`](uitextfield/inputview.md) property of text fields or text views to a view that should replace the system keyboard.

Creating a custom keyboard requires several steps. In addition to adding a Custom Keyboard extension target to your project, you have to configure options, implement your custom interface, and decide what text interactions to support. Users expect a variety of common keyboard interactions such as autocorrection, autocapitalization, smart quotes, and more.

##### Add a Custom Keyboard Target to Your App

The Custom Keyboard Extension template provides a starting point for you to build your keyboard extension. Xcode configures your project to build the extension and includes it in your app’s bundle.

1. Open your app project in Xcode.
2. Choose File > New > Target.
3. Select Custom Keyboard Extension from the Application Extension group.
4. Click Next.
5. Specify the name of your extension and configure the language and other options.
6. Click Finish.

![Screenshot of Xcode’s new target dialog with Custom Keyboard Extension highlighted.](https://docs-assets.developer.apple.com/published/5c33dbd2003e91541f0453a03e138c2f/media-3570733%402x.png)

Make sure the Display Name field in the General tab of your keyboard target accurately describes your keyboard. The Settings app uses this value in the list of third-party keyboards.

![Screenshot of the Identity section from Xcode’s Project editor showing the Display Name field. ](https://docs-assets.developer.apple.com/published/705644ded1016199b2092257ab518f05/media-3570265%402x.png)

If you support multiple languages that require different keyboard layout or functionality, repeat the steps above to add additional custom keyboard targets for each language. Set the `PrimaryLanguage` value accordingly in each of the target’s `Info.plist` files.

##### Configure Information Property List Options

If applicable to your custom keyboard, edit the keyboard extension’s `Info.plist` to configure the following options:

|  | Set this to [`true`](https://developer.apple.com/documentation/swift/true) if your keyboard is capable of generating standard ASCII characters. |
| --- | --- |
|  | If your keyboard primarily supports right to left languages, or if the insertion cursor should default to the right when editing in a text field, set this to [`true`](https://developer.apple.com/documentation/swift/true). |
|  | Set this to a string representing the primary language your keyboard supports. Use a two-character code like `nl` for Dutch, or language and country code such as `nl-BE` for Dutch in Belgium. The Settings app displays the primary language in the list of keyboards. |
|  | Set this to [`true`](https://developer.apple.com/documentation/swift/true) if your keyboard needs access to network resources, to write to a shared group container, or other capabilities. For more information, see [`Configuring open access for a custom keyboard`](configuring-open-access-for-a-custom-keyboard.md). |

Set these keys in the [`NSExtension`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension) > [`NSExtensionAttributes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes) dictionary of the `Info.plist` file:

![Screenshot showing the NSExtensionAttributes section in a custom keyboard target’s Info.plist file. ](https://docs-assets.developer.apple.com/published/94a9892ed497de8e7e52e95fe427b6fd/media-3570266%402x.png)

##### Add Your Custom User Interface

When the user activates your keyboard, it replaces the system keyboard. Your custom keyboard extension’s principal class provides the view that’s displayed. By default, Xcode’s custom keyboard template configures a class named `KeyboardViewController` as the principal class. This controller’s view is where you define your user interface.

> 💡 **Tip**:  For design guidance, see [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards).

 For design guidance, see [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/components/selection-and-input/onscreen-keyboards).

When designing your keyboard’s user interface, incorporate a button to switch keyboards. The system keyboard uses a button with a globe icon as shown in the following image.

![Screenshot showing the standard system keyboard.](https://docs-assets.developer.apple.com/published/0163b0e6d684e60e9d3cadfa08e83e4d/media-3570257%402x.png)

Use the [`needsInputModeSwitchKey`](uiinputviewcontroller/needsinputmodeswitchkey.md) property on [`UIInputViewController`](uiinputviewcontroller.md) to determine if you should display a button to switch keyboards. If the user has only one keyboard enabled, there’s no need to show a keyboard switching interface. On iPhones with Face ID, iOS automatically shows the globe icon below your keyboard view and sets this property to [`false`](https://developer.apple.com/documentation/swift/false), indicating that you shouldn’t show your button.

Configure your keyboard switching button with an action targeting the [`handleInputModeList(from:with:)`](uiinputviewcontroller/handleinputmodelist(from:with:).md) method of your input view controller subclass. The default custom keyboard template does this by adding an action to the button:

```swift
nextKeyboardButton.addTarget(self, action: #selector(handleInputModeList(from:with:)), for: .allTouchEvents)
```

Using [`allTouchEvents`](uicontrol/event/alltouchevents.md) allows the system to automatically show the keyboard list picker when the user long presses the button.

![Screenshot of the system keyboard after the user had long pressed the globe icon. The globe button displays a popup menu allowing the user to select between their enabled keyboards, or open Keyboard Settings.](https://docs-assets.developer.apple.com/published/4ad81e605c6c99663c3452b0278588db/media-3570259%402x.png)

Your keyboard should also be flexible with the layout because the width of the keyboard can vary, even while it’s currently on screen. All keyboards should support both compact and regular widths and allow for transitioning between the two. Test your keyboard in portrait and landscape orientations, and on iPadOS be sure to test your keyboard in a floating view.

![Screenshot showing a floating keyboard in iPadOS.](https://docs-assets.developer.apple.com/published/a962463f019041183abfcdeadfc95d06/media-3571051%402x.png)

For more details, see [`Configuring a custom keyboard interface`](configuring-a-custom-keyboard-interface.md).

##### Handle Text Interactions

Custom keyboards run in an isolated process that doesn’t have direct access to the text input view. [`UIInputViewController`](uiinputviewcontroller.md) provides a [`textDocumentProxy`](uiinputviewcontroller/textdocumentproxy.md) property allowing your keyboard to access the text input view. You use this proxy to get the selected text, insert or delete text, manipulate the text insertion position, and get surrounding textual context in order to support things like autocorrect or autocomplete.

```swift
// Insert a string into the text input view.
textDocumentProxy.insertText("Hello world.")

// Get the currently selected text
let selectedText = textDocumentProxy.selectedText
```

For more information, see [`Handling text interactions in custom keyboards`](handling-text-interactions-in-custom-keyboards.md).

##### Debug Your Custom Keyboard

Debugging a custom keyboard is similar to debugging any app extension. Xcode prompts you to choose a host app to launch, then you begin editing text in that host app in order to invoke your custom keyboard. The host app can be any app available in the run destination, including your app that contains the keyboard extension.

1. Select the build scheme for your keyboard extension target and a run destination (simulator or device).
2. Select Product > Run to begin your debugging session.
3. Xcode prompts you to select a host app. Choose an app that allows text input, like Notes. Xcode builds and installs your app with its keyboard extension, then launches the app you selected.
4. After the host app launches, begin editing a text field. The most recently used keyboard is shown.
5. Touch and hold the globe button to display the list of available keyboards. Choose your app’s keyboard.

iOS launches your keyboard extension in its own process, and Xcode attaches a debugging session to it. You can now set breakpoints and perform normal debugging tasks in your extension code.

> ❗ **Important**:  If your keyboard isn’t available in the list of active keyboards, you have to enable it. In Settings, navigate to General > Keyboard > Keyboards and select Add New Keyboard. Choose your keyboard(s) from the list of third-party keyboards.

 If your keyboard isn’t available in the list of active keyboards, you have to enable it. In Settings, navigate to General > Keyboard > Keyboards and select Add New Keyboard. Choose your keyboard(s) from the list of third-party keyboards.

##### Limit Memory Usage

Your custom keyboard code executes in a separate process, and that process has a limit on the amount of memory it may use. If your keyboard extension exceeds the memory limit the system terminates it. Here are some tips for managing memory efficiently:

- Test your keyboard on various device models. The memory limits vary from model to model.
- Be sure to handle low memory notifications. Release any resources that aren’t strictly necessary.
- Keep in mind that dismissing the keyboard won’t necessarily terminate the keyboard extension process. Don’t assume the system releases memory your keyboard is using when it’s no longer visible on screen.

For more information on crash logs related to memory usage limits, see [`Diagnosing issues using crash reports and device logs`](https://developer.apple.com/documentation/Xcode/diagnosing-issues-using-crash-reports-and-device-logs) and `EXC_CRASH (SIGQUIT)`.

## Topics

### Keyboard configuration
- [Configuring a custom keyboard interface](configuring-a-custom-keyboard-interface.md)
  Design a flexible, functional, and responsive interface for editing text.
- [Configuring open access for a custom keyboard](configuring-open-access-for-a-custom-keyboard.md)
  Enable network access and write access to a shared group container.
### Text interactions
- [Handling text interactions in custom keyboards](handling-text-interactions-in-custom-keyboards.md)
  Insert, delete, and manipulate text by using a proxy to a text input view.

## See Also

- [class UIInputViewController](uiinputviewcontroller.md)
  The primary view controller for a custom keyboard app extension.
- [class UIInputView](uiinputview.md)
  An object that displays and manages custom input for a view when that view becomes the first responder.
- [class UILexicon](uilexicon.md)
  A read-only array of term pairs, each in a lexicon entry object, for a custom keyboard.
- [class UILexiconEntry](uilexiconentry.md)
  A read-only term pair, available within a lexicon object, for a custom keyboard.
- [protocol UITextDocumentProxy](uitextdocumentproxy.md)
  An object that provides textual context to a custom keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/creating-a-custom-keyboard)*