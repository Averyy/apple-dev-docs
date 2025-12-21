# Building a Settings bundle for your app

**Framework**: Foundation

Integrate your app’s custom settings into the Settings app in iOS, iPadOS, tvOS, and visionOS, and support a Mac Catalyst settings window.

#### Overview

In iOS, iPadOS, tvOS, and visionOS, you can display some or all of your app’s settings from the system’s Settings app. The Settings app already displays system-specific settings for each app. For example, if an app supports push notifications, the Settings app displays details about the types of alerts the system uses to deliver those notifications. If you don’t want to display settings from your app’s interface, you can display them in the Settings app instead. Typically, you do so if people modify the settings infrequently.

To add custom settings to the system’s Settings app, include a Settings bundle inside your app. A  contains static files that describe your app’s settings to the system. The system uses the information in these files to build the content for your app’s settings interface and to save changes to settings back to your app’s defaults database. Your app’s custom settings appear below any system-specific settings.

If your iOS app supports Mac Catalyst, the system uses your app’s Settings bundle to create an appropriate settings interface when your app runs in macOS. The system displays and manages this settings interface for you, and automatically adds a menu item to your app’s menus to display that interface. This system-provided settings interface matches the experience that people expect for apps in macOS.

> **Note**: To determine when to add a Settings bundle to your app, see [`Settings`](https://developer.apple.com/design/Human-Interface-Guidelines/settings) in Human Interface Guidelines.

##### Add the Settings Bundle and Initial Content to Your Project

Xcode provides a template for a Settings bundle that you can add to your project and modify. To add this bundle to your app:

1. Open your app project in Xcode.
2. Select New > File from Template.
3. Select Settings Bundle from the Resources section.
4. Click Next.
5. Add the Settings bundle to your app target.
6. Save the bundle with the name `Settings.bundle`.

When you add a Settings bundle to your project, Xcode creates the bundle directory and populates it with some initial files. The main file of each Settings bundle is a property list file called `Root.plist` that describes the contents of the main page of your settings interface. This property list file contains a dictionary with special keys and values that describe your interface. Place the individual elements of your settings interface in the array for the Preference Items key. Use other keys to configure both the page of content and the elements themselves.

Remove any elements from the initial `Root.plist` file that you don’t need, and replace them with elements you do need. The following table lists the types of elements you can include, along with tips for how to use them to display your app’s settings.

| Element type | Purpose |
| --- | --- |
| [`Add a child page element`](building-a-settings-bundle-for-your-app#Add-a-child-page-element.md) | An element that displays a separate page of settings. Use this element to organize large numbers of settings. |
| [`Add a group element`](building-a-settings-bundle-for-your-app#Add-a-group-element.md) | An element that marks the beginning of a related set of elements. The Settings app groups the elements that follow visually and applies a title you provide to the group. |
| [`Add a multi-value element`](building-a-settings-bundle-for-your-app#Add-a-multi-value-element.md) | An element that occupies a single row on the page. When someone taps or clicks this element, it displays a new page with a mutually exclusive set of choices. This element provides a more visually compact version of a radio group. |
| [`Add a radio group element`](building-a-settings-bundle-for-your-app#Add-a-radio-group-element.md) | An element that displays a group of mutually exclusive choices on the current page. This element is similar to a multi-value element but without the extra navigation. |
| [`Add a slider element`](building-a-settings-bundle-for-your-app#Add-a-slider-element.md) | An element that lets someone select a single numerical value from a range of values. |
| [`Add a text-field element`](building-a-settings-bundle-for-your-app#Add-a-text-field-element.md) | An element that displays a setting’s name and an editable text field. Use it to capture text-based content. |
| [`Add a title element`](building-a-settings-bundle-for-your-app#Add-a-title-element.md) | An element that displays a read-only setting’s name and value. Use this element to display setting information that you don’t want someone to change. |
| [`Add a toggle switch element`](building-a-settings-bundle-for-your-app#Add-a-toggle-switch-element.md) | An element that offers a binary choice. Use it to enable or disable features. |

##### Localize the Content of Your Settings Interface

When you build your settings interface, specify the text for interface elements in your development language. To localize that text, add strings files to your Settings bundle for each language you support. When building your settings interface, the Settings app loads the strings file for the appropriate language and makes the relevant substitutions. The following listing shows the structure of a bundle that includes localized strings for English and German.

```None
Settings.bundle/
    Root.plist
    en.lproj/
        root.strings
    de.lproj/
        root.strings 
```

Each property list file in your Settings bundle can have its own dedicated strings file. When building a page of settings, add the Strings Filename key to the page and set its value to the name of the relevant strings file. Omit the filename extension from the name of the strings file. For example, when specifying the strings file for the `Root.plist` file in the previous listing, set the value of the key to `root`.

Inside each strings file, place a pair of translation strings on its own line and separate the strings with an equal sign (=). Place the original value on the left side of the equal sign, and have your translator place the translated value on the right side. The following listing shows the contents of a strings file that translates a set of strings from English to German.

```None
"Group" = "Gruppe";
"Name" = "Name";
"Enabled" = "Aktiviert";
```

##### Specify the Contents of Each Settings Page

Each property list file in your Settings bundle contains top-level keys that describe the contents of that page. Include these keys in the `Root.plist` file to specify the contents of your main settings page. Also include them in the property list file for any child pages you add to your Settings bundle. The keys tell the Settings app what elements to display on the page and where to find localized resources. The following table lists the supported keys and their purpose.

| Key name | Data type | Description |
| --- | --- | --- |
| Preference Items (required) | Array | The elements to display on the current page. Each item in the array is a Dictionary with the keys and values for a single element. Arrange items in the array in the same order you want them to appear on the page. The raw name of this key is `PreferenceSpecifiers`. |
| Strings Filename | String | The name of the `.strings` file, without the filename extension, you use to store localized text for the current page. For each language you support, create language-specific project directories in your Settings bundle and place a copy of this file in the directory. If you omit this key, the system doesn’t display a localized version of your settings interface. The raw name of this key is `StringsTable`. |
| Settings Page Title | String | The name of the page, which the Settings app doesn’t use. The raw name of this key is `Title`. |

##### Add a Child Page Element

If your app’s settings interface includes a large number of elements, organize those elements hierarchically using child page elements. When the Settings app encounters a child page element, it adds a single row to the current page of your settings interface. Tapping or clicking the row transitions to a new page, the contents of which you provide in a separate property list file in your Settings bundle. The following table lists the supported keys and their purpose.

| Key name | Value type | Description |
| --- | --- | --- |
| Type (required) | String | The value of this key is always `Child Pane`.  The raw name of this key is `Type` and the raw value is `PSChildPaneSpecifier`. |
| Title (required, localizable) | String | The title string that the system displays next to the text field. The raw name of this key is `Title`. |
| Filename (required) | String | The name of the property list file to load. Specify the filename without its `.plist` extension. Place the file in the root directory of your Settings bundle, alongside the existing `Root.plist` file. The raw name of this key is `File`. |
| Icon | String | The name of an image in your Settings bundle, without the filename extension. In an iOS app running in Mac Catalyst, the system displays this image as the toolbar tab icon in your app’s Settings window. The Settings apps in iOS, iPadOS, tvOS, and visionOS ignore this key. The raw name of this key is `Icon`. |

##### Add a Group Element

Include group elements to separate settings visually on the current page. When the Settings app encounters a group element, it renders the items in the group with a special visual treatment to indicate they’re related to each other, and not to other elements. The group includes the items immediately after the group element. The group ends when there are no more elements in the Preference Items array, or when the Settings app encounters a radio group element or another group element. The following table lists the supported keys and their purpose.

| Key name | Value type | Description |
| --- | --- | --- |
| Type (required) | String | The value of this key is always `Group`.  The raw name of this key is `Type` and the raw value is `PSGroupSpecifier`. |
| Title (localizable) | String | The title string to display before the grouped items. Use this key to specify the purpose of the group of settings. The raw name of this key is `Title`. |

##### Add a Multi Value Element

A multi-value element gives someone a way to choose one value from a mutually exclusive set of values. The Settings app displays a single row for this element on the current page. When someone taps or clicks that row, Settings displays a new page with the available values and places a checkmark next to the selected one. When someone changes the selected value, the system saves the new value to your app’s defaults database. The following table lists the supported keys and their purpose.

| Key name | Value type | Description |
| --- | --- | --- |
| Type (required) | String | The value of this key is always `Multi Value`.  The raw name of this key is `Type` and the raw value is `PSMultiValueSpecifier`. |
| Identifier (required) | String | The name of a key in your app’s defaults database. When someone updates the setting, the system writes the new value to this key in the defaults database. The raw name of this key is `Key`. |
| Title (required, localizable) | String | The text to display on the leading edge of the item’s row. The trailing edge of the row contains the currently selected value, if any, and a chevron to indicate that tapping or clicking the row displays a new page. The raw name of this key is `Title`. |
| Default Value (required) | Boolean | The default selected value, if needed. If the defaults database doesn’t contain a value for the specified identifier, the Settings app uses this value. The raw name of this key is `DefaultValue`. |
| Titles (required, localizable) | Array | An array of strings, each of which contains a human-readable description of one option. Each string in this array corresponds to the value at the same index in the Values array. The Values array must have the same number of elements. The raw name of this key is `Titles`. |
| Values (required) | Array | An array of values for the corresponding options. The items in the array can be any property list type. When someone chooses an option, the system writes the corresponding value from this array to the defaults database. This array must have the same number of elements as the Title array. The raw name of this key is `Values`. |

##### Add a Radio Group Element

A radio group element displays a group of mutually exclusive values on the current page. This element is similar to a multi-value element but places the items on the current page instead of displaying a new page. Tapping or clicking one row deselects the other rows and saves the new value to your app’s defaults database. Avoid using this option with a large number of possible values. The following table lists the supported keys and their purpose.

| Key name | Value type | Description |
| --- | --- | --- |
| `Type` (required) | String | The raw name of this key is `Type` and the value is always `PSRadioGroupSpecifier`. |
| `Identifier` (required) | String | The name of a key in your app’s defaults database. When someone updates the setting, the system writes the new value to this key in the defaults database. The raw name of this key is `Key`. |
| `Title` (localizable) | String | The text to display for the group name. The Settings app places this text above the group of options. Use this string to convey the purpose of the group. The raw name of this key is `Title`. |
| `FooterText` (localizable) | String | Additional text to display below the group box. The raw name of this key is `FooterText`. |
| `DefaultValue` (required) | Boolean | The default selected value, if needed. If the defaults database doesn’t contain a value for the specified identifier, the Settings app uses this value. The raw name of this key is `DefaultValue`. |
| `Titles` (required, localizable) | Array | An array of strings, each of which contains a human-readable description of one option. Each string in this array corresponds to the value at the same index in the Values array. The Values array must have the same number of elements. The raw name of this key is `Titles`. |
| `Values` (required) | Array | An array of values for the corresponding options. The items in the array can be any property list type. When someone chooses an option, the system writes the corresponding value from this array to the defaults database. This array must have the same number of elements as the Title array. The raw name of this key is `Values`. |

If a group element appeared previously in the list of items, the presence of this element ends that group and creates a new group exclusively for the radio group values. If you display any items after the radio group, make the first item another group element to create a new group of settings.

##### Add a Slider Element

A slider element displays a row with a slider control that you can use to represent a continuous range of values. The control in this row is equivalent to a [`Slider`](https://developer.apple.com/documentation/SwiftUI/Slider), [`UISlider`](https://developer.apple.com/documentation/UIKit/UISlider), or [`NSSlider`](https://developer.apple.com/documentation/AppKit/NSSlider) control. The slider control spans the entire width of the row, with the slider’s minimum position located at the leading edge of the row. The following table lists the supported keys and their purpose.

| Key name | Value type | Description |
| --- | --- | --- |
| Type (required) | String | The value of this key is always `Slider`.  The raw name of this key is `Type` and the raw value is `PSSliderSpecifier`. |
| Identifier (required) | String | The name of a key in your app’s defaults database. When someone updates the setting, the system writes the new value to this key in the defaults database. The raw name of this key is `Key`. |
| Default Value (required) | Boolean | The default value, if needed. If the defaults database doesn’t contain a value for the specified identifier, the Settings app uses this value. The raw name of this key is `DefaultValue`. |
| Minimum Value (required) | Number | The numerical value to store in the defaults database when the slider thumb is at its minimum position. The raw name of this key is `MinimumValue`. |
| Maximum Value (required) | Number | The numerical value to store in the defaults database when the slider thumb is at its maximum position. The raw name of this key is `MaximumValue`. |
| Min Value Image Filename | String | The name of an image in your Settings bundle, without the filename extension. The Settings app displays this image next to the slider’s minimum position, and scales the image to fit the available space as needed. The raw name of this key is `MinimumValueImage`. |
| Max Value Image Filename | String | The name of an image in your Settings bundle, without the filename extension. The Settings app displays this image next to the slider’s maximum position, and scales the image to fit the available space as needed. The raw name of this key is `MaximumValueImage`. |

> **Note**: tvOS doesn’t support slider controls in settings interfaces, and the Settings app in tvOS ignores slider elements in your property list files.

##### Add a Text Field Element

A text-field element displays a row with an editable space for typing a text-based value. The title of the element appears on the row’s leading edge and the value appears on the trailing edge. Tapping or clicking the row displays the system keyboard so the person can type. The following table lists the supported keys and their purpose.

| Key name | Value type | Description |
| --- | --- | --- |
| Type (required) | String | The value of this key is always `Text Field`.  The raw name of this key is `Type` and the raw value is `PSTextFieldSpecifier`. |
| Identifier (required) | String | The name of a key in your app’s defaults database. When someone updates the setting, the system writes the new value to this key in the defaults database. The raw name of this key is `Key`. |
| Title (localizable) | String | The text to display in the leading edge of the row. Use this value to describe the purpose of the setting. If you omit this key, the editable text field spans the width of the row. The raw name of this key is `Title`. |
| Default Value | Boolean | The default value, if needed. If the defaults database doesn’t contain a value for the specified identifier, the Settings app uses this value. The raw name of this key is `DefaultValue`. |
| Text Field Is Secure | Boolean | A Boolean value that indicates whether to hide the typed text. Set the value of this key to `YES` to hide the text, or `NO` to show the text as someone types it. If you omit this key, the Settings app sets it to `NO`. The raw name of this key is `IsSecure`. |
| Keyboard Type | String | The type of keyboard to display. Set the value of this key to one of the following strings: `Alphabet`, `NumbersAndPunctuation`, `NumberPad`, `URL`, or `EmailAddress`. These values correspond to keyboard types available for use with standard text field controls. If you omit this key, the Settings app sets the keyboard type to `Alphabet`. The raw name of this key is `KeyboardType`. |
| Autocapitalization Style | String | The autocapitalization approach to take during typing. Set the value of this key to one of the following values: `None`, `Sentences`, `Words`, or `AllCharacters`. These values correspond to the autocapitalization styles for the system’s text input traits. If you omit this key, the Settings app uses the `None` style. The raw name of this key is `AutocapitalizationType`. |
| Autocorrection Style | String | The autocorrect style to apply to typed text. Set the value of this key to one of the following values: `Default`, `Yes`, or `No`. These values correspond to the autocorrection behaviors for the system’s text input traits. If you omit this key, the Settings app uses the `Default` style. The raw name of this key is `AutocorrectionType`. |

> ❗ **Important**: Because the Settings app displays and manages your settings interface, your app can’t validate the setting’s text before the system saves it to the database. When you retrieve a value for the associated setting in your code, validate it before you use it.

##### Add a Title Element

A title element displays a read-only version of the setting’s name and its currently configured value, if any. Use this element to display settings that you don’t want people to change. For example, you might use this field to display login information that someone created using your app’s interface. The following table lists the supported keys and their purpose.

| Key name | Value type | Description |
| --- | --- | --- |
| Type (required) | String | The value of this key is always `Title`.  The raw name of this key is `Type` and the raw value is `PSTitleValueSpecifier`. |
| Identifier (required) | String | The name of a key in your app’s defaults database. When someone updates the setting, the system writes the new value to this key in the defaults database. The raw name of this key is `Key`. |
| Title (required, localizable) | String | The text to display in the leading edge of the row. Use this value to describe the purpose of the setting. The raw name of this key is `Title`. |
| Default Value (required) | String | The default selected value, if needed. If the defaults database doesn’t contain a value for the specified identifier, the Settings app uses this value. The raw name of this key is `DefaultValue`. |
| Titles (localizable) | Array | An array of strings, each of which contains a human-readable description of one option. Each string in this array corresponds to the value at the same index in the Values array. The Values array must have the same number of elements. The raw name of this key is `Titles`. |
| Values | Array | An array of values for the specified options. The values in this array can be any property-list type. This array must have the same number of elements as the Title array. The raw name of this key is `Values`. |

Use the Titles and Values keys of this element to provide meaningful descriptions of potentially cryptic settings. If the Values array contains the current setting, the Settings app displays the associated string from the Titles array instead. If the setting contains a value that’s not in the array, the Settings app displays the value without modification.

##### Add a Toggle Switch Element

A toggle switch element displays a control with a binary choice and a title describing the meaning behind that choice. This element is equivalent to a [`Toggle`](https://developer.apple.com/documentation/SwiftUI/Toggle), [`UISwitch`](https://developer.apple.com/documentation/UIKit/UISwitch), or [`NSSwitch`](https://developer.apple.com/documentation/AppKit/NSSwitch) control. Typically, you use this element for settings that enable or disable features. The following table lists the supported keys and their purpose.

| Key name | Value type | Description |
| --- | --- | --- |
| Type (required) | String | The value of this key is always `Toggle Switch`.  The raw name of this key is `Type` and the raw value is `PSToggleSwitchSpecifier`. |
| Title (required, localizable) | String | The text to display at the leading edge of the row. The Settings app places the switch control at the trailing edge of the row. The raw name of this key is `Title`. |
| Identifier (required) | String | The name of a key in your app’s defaults database. When someone updates the setting, the system writes the new value to this key in the defaults database. The raw name of this key is `Key`. |
| Default Value (required) | Boolean | The default value, if needed. If the defaults database doesn’t contain a value for the specified identifier, the Settings app uses this value. The raw name of this key is `DefaultValue`. |
| Value for ON | Any | The value to store in the defaults database when the switch is in the “on” position. Include this key to store a non-Boolean value in the defaults database.  For example, you might set this value to a string with the text “ON”. The raw name of this key is `TrueValue`. |
| Value for OFF | Any | The value to store in the defaults database when the switch is in the “off” position. Include this key to store a non Boolean value in the defaults database. For example, you might set this value to a string with the text “OFF”. The raw name of this key is `FalseValue`. |
| Description | String | A longer descriptive string to display under a toggle switch in macOS. This key applies only to iOS apps running in Mac Catalyst; other platforms ignore it. The raw name of this key is `Description`. |
| `TrueConfirmationPrompt` | Dictionary | A dictionary that defines the prompt to display when someone tries to set the switch to the “on” position. This key applies only to iOS apps running in Mac Catalyst; other platforms ignore it. |
| `FalseConfirmationPrompt` | Dictionary | A dictionary that defines the prompt to display when someone tries to set the switch to the “off” position. This key applies only to iOS apps running in Mac Catalyst; other platforms ignore it. |

In an iOS app running in Mac Catalyst, include the `TrueConfirmationPrompt` or `FalseConfirmationPrompt` keys if you want the person to confirm the change before the system updates the setting. When these keys are present, the system displays a prompt with information you provide in the dictionary of the appropriate key. If the person confirms the change, the system writes the new setting to the defaults database. The following table lists the supported keys and values for that dictionary.

| Key name | Value type | Description |
| --- | --- | --- |
| `Type` (required) | String | The value of this key must be `PSConfirmationPrompt`. |
| `Title` (required) | String | A string with the title of the prompt. This title might not appear on some devices. |
| `Prompt` (required) | String | Explanatory text that the prompt displays to confirm the toggle change. Use this string to ask the person to confirm the choice. |
| `ConfirmText` | String | The text to display in the prompt’s confirmation button. If the person clicks this button, the system changes the setting to the new value. If you don’t provide this key, the system provides a default title for the button. |
| `DenyText` | String | The text to display in the prompt’s cancel button. If the person clicks this button, the system doesn’t change the setting. If you don’t provide this key, the system provides a default title for the button. |

## See Also

- [Adding a settings interface to your app](adding-a-settings-interface-to-your-app.md)
  Create a dedicated interface to display and modify your app’s settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/building-a-settings-bundle-for-your-app)*