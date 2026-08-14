# UIPhotoSearchSuggestion

**Framework**: UIKit  
**Kind**: class

An input suggestion that carries photo search metadata for people, subjects, locations, and time periods.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
class UIPhotoSearchSuggestion
```

#### Discussion

When someone types text that could match a photo library search, such as “photos from Paris last summer,” the system recognizes the input as a photo library search and delivers a `UIPhotoSearchSuggestion` through the [`textField(_:insertInputSuggestion:)`](uitextfielddelegate/textfield(_:insertinputsuggestion:).md) or [`textView(_:insertInputSuggestion:)`](uitextviewdelegate/textview(_:insertinputsuggestion:).md) delegate method. Use `as? UIPhotoSearchSuggestion` to check whether the incoming [`UIInputSuggestion`](uiinputsuggestion.md) is a photo search suggestion and access its metadata.

After receiving a suggestion, you have two options: Pass the object directly to the [`Photos`](https://developer.apple.com/documentation/photos) framework to present a pre-populated photo picker, or read the `whoValues`, `whatValues`, `whereValues`, and `whenValues` arrays to build a custom search experience.

You can’t create a `UIPhotoSearchSuggestion` directly. The system creates and delivers instances through the input suggestion system.

##### Presenting a Photo Picker

Pass the suggestion to `PHPickerSearchText(photoSearchSuggestion:)` to pre-populate a `PHPickerViewController` with photos matching the person’s search.

```swift
class SearchViewController: UIViewController, UITextFieldDelegate, PHPickerViewControllerDelegate {
    @IBOutlet var searchField: UITextField!

    func textField(_ textField: UITextField,
                   insertInputSuggestion inputSuggestion: UIInputSuggestion) {
        if let photoSuggestion = inputSuggestion as? UIPhotoSearchSuggestion {
            presentPhotosPicker(with: photoSuggestion)
        }
    }

    func presentPhotosPicker(with suggestion: UIPhotoSearchSuggestion) {
        var configuration = PHPickerConfiguration()
        configuration.searchText = PHPickerSearchText(photoSearchSuggestion: suggestion)
        let picker = PHPickerViewController(configuration: configuration)
        picker.delegate = self
        present(picker, animated: true)
    }

    func picker(_ picker: PHPickerViewController,
                didFinishPicking results: [PHPickerResult]) {
        dismiss(animated: true)
        // Handle selected photos.
    }
}
```

##### Building a Custom Search

If your app has its own photo search UI, read the filter arrays and construct your own query.

```swift
func textField(_ textField: UITextField,
               insertInputSuggestion inputSuggestion: UIInputSuggestion) {
    guard let suggestion = inputSuggestion as? UIPhotoSearchSuggestion else { return }

    // Build a custom query from the individual filter values.
    let who = suggestion.whoValues        // e.g., ["John"]
    let what = suggestion.whatValues      // e.g., ["hiking"]
    let locations = suggestion.whereValues // e.g., ["Paris"]
    let timeframes = suggestion.whenValues // e.g., ["last summer"]

    performCustomPhotoSearch(people: who, subjects: what, locations: locations, timeframes: timeframes)
}
```

## Topics

### Instance Properties
- [var whatValues: [String]](uiphotosearchsuggestion/whatvalues.md)
  Subjects or topics mentioned in the text that can be used to filter photos.
- [var whenValues: [String]](uiphotosearchsuggestion/whenvalues.md)
  Time periods mentioned in the text that can be used to filter photos.
- [var whereValues: [String]](uiphotosearchsuggestion/wherevalues.md)
  Locations mentioned in the text that can be used to filter photos.
- [var whoValues: [String]](uiphotosearchsuggestion/whovalues.md)
  People mentioned in the text that can be used to filter photos.

## Relationships

### Inherits From
- [UIInputSuggestion](uiinputsuggestion.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Adopting Smart Reply in your messaging or email app](adopting-smart-reply-in-your-messaging-or-email-app.md)
  Generate reply suggestions by using Apple Intelligence and put selected text into your text UI.
- [class UIConversationContext](uiconversationcontext.md)
  A base class that represents a conversation between participants, such as in an email or messaging app.
- [UIConversationContext.Entry](uiconversationcontext/entry.md)
  A base class that represents a message in a conversation.
- [class UIMailConversationContext](uimailconversationcontext.md)
  A class that represents an email conversation.
- [UIMailConversationContext.MailEntry](uimailconversationcontext/mailentry.md)
  A class that represents a specific email in an email thread.
- [class UIMessageConversationContext](uimessageconversationcontext.md)
  A class that represents a message conversation.
- [UIMessageConversationContext.MessageEntry](uimessageconversationcontext/messageentry.md)
  A class that represents a message in a message conversation.
- [class UIInputSuggestion](uiinputsuggestion.md)
  A base class you use to handle suggestions from the keyboard or system.
- [class UISmartReplySuggestion](uismartreplysuggestion.md)
  A class you use to handle a Smart Reply suggestion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiphotosearchsuggestion)*