# Supporting suggestions in your app’s share extension

**Framework**: Foundation

Make your messaging app available for share sheet suggestions and use SiriKit intents to populate your app’s share extension.

#### Overview

Using the iOS share sheet, people can launch your messaging app instantly from a list of suggestions when sharing content like a link, image, video, or file. The share sheet suggests conversations with people in apps that a person interacts with frequently, and updates its suggestions over time based on a person’s favorite apps and conversations. When a person shares an image in iOS 16 or later, the share sheet prioritizes conversations with people it identifies in the image.

![A screenshot of an iPhone. The upper half shows the apple.com website in Safari. The bottom half of the screen shows the share sheet after the person has decided to share the website with someone. iOS suggests conversations in the Messages app and another app.](https://docs-assets.developer.apple.com/published/24f21db9d18dea3833cb532a279ceb63/media-4323287%402x.png)

To allow iOS to include conversations from your messaging app in the list of suggestions:

- Add a share extension to your app as described in [`Understand Share Extensions`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/Share.html#//apple_ref/doc/uid/TP40014214-CH12-SW2).
- Declare support for the [`INSendMessageIntent`](https://developer.apple.com/documentation/Intents/INSendMessageIntent) intent type.
- Donate an [`INSendMessageIntent`](https://developer.apple.com/documentation/Intents/INSendMessageIntent) in your messaging app and its share extension.

As a person selects an app from the list of suggestions, the app’s sharing interface, implemented as a share extension, accesses additional metadata. iOS provides the [`INSendMessageIntent`](https://developer.apple.com/documentation/Intents/INSendMessageIntent) for you to prepopulate the interface of your app’s share extension. For example, you can access the [`conversationIdentifier`](https://developer.apple.com/documentation/Intents/INSendMessageIntent/conversationIdentifier) property and preselect a conversation to share content so a person doesn’t need to search for a contact in a list or type a friend’s name.

A screenshot of an iPhone with the Safari browser displaying the apple.com homepage. The person tapped the Share button and selected an app from the list of suggestions. The platforms default sharing interface, based on an SLComposeViewController, is visible. Based on the available metadata, the extension has prepopulated the interface with a recipient (Juan Chavez).

![A screenshot of an iPhone with the Safari browser displaying the apple.com homepage. The person tapped the Share button and selected an app from the list of suggestions. The platforms default sharing interface, based on an SLComposeViewController, is visible. Based on the available metadata, the extension has prepopulated the interface with a recipient (Juan Chavez).](https://docs-assets.developer.apple.com/published/dd614115375e87041ed829b27bee9335/media-3379657%402x.png)

##### Add a Share Extension to Your App

To add a share extension to your app, open your app’s project in Xcode and select File > New > Target from the menu bar. Xcode presents a sheet that contains templates for different kinds of targets. Select the share extension template from the iOS pane and follow the steps in Xcode’s interface to add one to your app. For more information, see [`Understand Share Extensions`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/Share.html#//apple_ref/doc/uid/TP40014214-CH12-SW2) in the App Extension Programming Guide.

##### Support the Send Message Intent

Open the Share extension’s `Info.plist`, and expand the [`NSExtension`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension) and [`NSExtensionAttributes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes) keys. Add a new entry with the [`IntentsSupported`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension/IntentsSupported) key and select `Array` for its value type. Add the string `INSendMessageIntent` as a new value to the array to declare support for the [`INSendMessageIntent`](https://developer.apple.com/documentation/Intents/INSendMessageIntent) intent type.

![A screenshot of Xcode showing the Info.plist file for a Share extension that the developer created using Xcode’s share extension template. The entries below the NSExtension key are expanded and show the IntentsSupported key with an item that has the value set to INSendMessageIntent. The NSExtensionActivationRule entry is set to TRUEPREDICATE.](https://docs-assets.developer.apple.com/published/e1b3d2a70f0387e00438023540fcd129/media-3358270%402x.png)

To make debugging easier, set the value of [`NSExtensionActivationRule`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes/NSExtensionActivationRule) to `TRUEPREDICATE` when you first add a share extension using Xcode’s template. Replace it with valid activation rules as described in [`Declaring Supported Data Types for a Share or Action Extension`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/ExtensionScenarios.html#//apple_ref/doc/uid/TP40014214-CH21-SW8) before submitting your app for review.

##### Donate a Send Message Intent

Donate an [`INSendMessageIntent`](https://developer.apple.com/documentation/Intents/INSendMessageIntent) only when a person sends or receives a message in your app and its share extension. Donate a [`CNContact`](https://developer.apple.com/documentation/Contacts/CNContact) along with [`INSendMessageIntent`](https://developer.apple.com/documentation/Intents/INSendMessageIntent) for [`sender`](https://developer.apple.com/documentation/Intents/INSendMessageIntent/sender) and [`recipients`](https://developer.apple.com/documentation/Intents/INSendMessageIntent/recipients) by adding values to the contact [`contactIdentifier`](https://developer.apple.com/documentation/Intents/INPerson/contactIdentifier) field when initializing an [`INPerson`](https://developer.apple.com/documentation/Intents/INPerson).

As you initialize the [`INSendMessageIntent`](https://developer.apple.com/documentation/Intents/INSendMessageIntent) object, provide metadata that’s available later when a person choses your app’s share extension from the list of suggestions. The following code snippet donates an [`INSendMessageIntent`](https://developer.apple.com/documentation/Intents/INSendMessageIntent) with a [`speakableGroupName`](https://developer.apple.com/documentation/Intents/INSendMessageIntent/speakableGroupName), a [`conversationIdentifier`](https://developer.apple.com/documentation/Intents/INSendMessageIntent/conversationIdentifier), and an [`INImage`](https://developer.apple.com/documentation/Intents/INImage).

```swift
// Create an INSendMessageIntent to donate an intent for a conversation with Juan Chavez.
let groupName = INSpeakableString(spokenPhrase: "Juan Chavez")
let sendMessageIntent = INSendMessageIntent(recipients: nil,
                                            content: nil,
                                            speakableGroupName: groupName,
                                            conversationIdentifier: "sampleConversationIdentifier",
                                            serviceName: nil,
                                            sender: nil)

// Add the person's avatar to the intent.
let image = INImage(named: "Juan Chavez")
sendMessageIntent.setImage(image, forParameterNamed: \.speakableGroupName)

// Donate the intent.
let interaction = INInteraction(intent: sendMessageIntent, response: nil)
interaction.donate(completion: { error in
    if error != nil {
        // Add error handling here.
    } else {
        // Do something, for example, send the content to a contact.
    }
})
```

When iOS includes a conversation within your app as a suggestion in the share sheet, it displays your app’s icon along with the [`INImage`](https://developer.apple.com/documentation/Intents/INImage) you associated with your [`INSendMessageIntent`](https://developer.apple.com/documentation/Intents/INSendMessageIntent). If there’s no [`INImage`](https://developer.apple.com/documentation/Intents/INImage) set on the intent, iOS uses the [`image`](https://developer.apple.com/documentation/Intents/INPerson/image) property from the [`INPerson`](https://developer.apple.com/documentation/Intents/INPerson) object for each recipient. If the [`INPerson`](https://developer.apple.com/documentation/Intents/INPerson) object’s [`image`](https://developer.apple.com/documentation/Intents/INPerson/image) is `nil`, iOS looks up the corresponding contact in the Contacts app using a person’s [`contactIdentifier`](https://developer.apple.com/documentation/Intents/INPerson/contactIdentifier). The share sheet then uses the contact’s image.

When a person shares an image in iOS 16 or later with the suggestions from Apple setting enabled, the share sheet prioritizes displaying conversations with people the system identifies in the image in the suggestions list. Include an [`INImage`](https://developer.apple.com/documentation/Intents/INImage) with the sharing intent you donate, so the system can attempt to identify people in the image. Provide an image that’s at least 360 pixels tall or wide to improve matching.

> 💡 **Tip**:  Both your app and its share extension donate an [`INSendMessageIntent`](https://developer.apple.com/documentation/Intents/INSendMessageIntent). Write reusable code by creating an object that donates the intent and is available to both the extension and the app.

##### Populate Your Share Extensions Interface with Metadata

When a person selects your app from the list of suggestions, you can access the metadata that you created when your app donated the [`INSendMessageIntent`](https://developer.apple.com/documentation/Intents/INSendMessageIntent). Use it to populate your share extension’s interface.

The following code listing shows a template implementation for an [`SLComposeServiceViewController`](https://developer.apple.com/documentation/Social/SLComposeServiceViewController) subclass. It accesses the [`intent`](nsextensioncontext/intent.md) property, makes sure it’s an [`INSendMessageIntent`](https://developer.apple.com/documentation/Intents/INSendMessageIntent), and uses the intent’s [`conversationIdentifier`](https://developer.apple.com/documentation/Intents/INSendMessageIntent/conversationIdentifier) to create a new `Recipient` object. It then uses the `Recipient` object to populate the share extension’s interface in the [`configurationItems()`](https://developer.apple.com/documentation/Social/SLComposeServiceViewController/configurationItems()) method.

```swift
import Intents
import Social
import UIKit

class ShareViewController: SLComposeServiceViewController {

    var recipient: Recipient = Recipient(withName: "Placeholder")
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Populate the recipient property with the metadata in case the person taps a suggestion from the share sheet.
        let intent = self.extensionContext?.intent as? INSendMessageIntent
        if intent != nil {
            let conversationIdentifier = intent!.conversationIdentifier
            self.recipient = recipient(identifier: conversationIdentifier!)
        }
    }

    func recipient(identifier: String) -> Recipient {
        // Create a recipient object, for example, by loading it from a data base.
        return Recipient(withName: identifier)
    }

    override func isContentValid() -> Bool {
        // Validate contentText and NSExtensionContext attachments here.
        return true
    }

    override func didSelectPost() {
        // This is called after the person selects Post. Upload contentText and NSExtensionContext attachments.
        
        // Inform the host that the selection is done, so it unblocks its UI.
        // Note: Alternatively, you could call super's -didSelectPost, which similarly completes the extension context.
        self.extensionContext!.completeRequest(returningItems: [], completionHandler: nil)
    }

    override func configurationItems() -> [Any]! {
        // To add configuration options via table cells at the bottom of the sheet, return an array of SLComposeSheetConfigurationItem here.
        
        // Use the Recipient object to populate the share sheet.
        let item = SLComposeSheetConfigurationItem()
        item?.title = NSLocalizedString("To:", comment: "The To: label when sharing content.")
        item?.value = self.recipient.name
        item?.tapHandler = {
            self.validateContent()
            item!.value = self.recipient.name
        }
        
        return [item!]
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/supporting-suggestions-in-your-app-s-share-extension)*