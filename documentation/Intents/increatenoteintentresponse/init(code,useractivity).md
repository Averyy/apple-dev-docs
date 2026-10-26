# init(code:userActivity:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the response object with the specified code and user activity object.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INCreateNoteIntentResponse is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
init(code: INCreateNoteIntentResponseCode, userActivity: NSUserActivity?)
```

```objc
- (instancetype) initWithCode:(INCreateNoteIntentResponseCode) code userActivity:(NSUserActivity *) userActivity;
```

#### Return Value

An initialized response object or `nil` if the object could not be created.

#### Discussion

After initializing the response object, put the note details into the [`createdNote`](./creatednote.md) property of the object.

When your app creates the note successfully, Siri displays information about the created note to the user. If the user chooses to view the new note in your app, SiriKit does not launch your app using the value in the `userActivity` parameter. Instead, SiriKit creates a new [`NSUserActivity`](../../Foundation/nsuseractivity.md) object whose interaction property contains an [`INSearchForNotebookItemsIntent`](../insearchfornotebookitemsintent.md) object. The value of that intent’s [`notebookItemIdentifier`](../insearchfornotebookitemsintent/notebookitemidentifier.md) property is the identifier of the note that you provided in the [`createdNote`](./creatednote.md) property of your response object.

## Parameters

- `code`: The response code indicating your success or failure in handling the intent. For a list of possible values, see [`INCreateNoteIntentResponseCode`](../increatenoteintentresponsecode.md).
- `userActivity`: The user activity object to use when launching your app. Provide an object if you want to add app-specific information. If you specify `nil`, the system automatically creates a user activity object for you, sets its type to the class name of the intent being handled, and fills it with an [`INInteraction`](../ininteraction.md) object containing the intent and your response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatenoteintentresponse/init(code:useractivity:))*