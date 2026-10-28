# userActivity

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The user activity object to use when launching the app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var userActivity: NSUserActivity? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSUserActivity * userActivity;
```

## Discussion

When initializing a response object, you can provide a custom user activity object with details about your response. You might specify a custom object when you want to customize the activity type string, add details to the [`userInfo`](../../Foundation/nsuseractivity/userinfo.md) dictionary, or customize any other properties of the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object.

If SiriKit determines that it needs to launch your app, either to handle the intent or respond to errors, it launches your app and delivers your user activity object. (Prior to delivery, SiriKit fills the [`interaction`](../../Foundation/nsuseractivity/interaction.md) property of the user activity object with the intent and your response.) In your app, use the information in the provided user activity object to take whatever actions are appropriate.

If the value of this property is `nil`, SiriKit creates a default user activity object and sets the [`activityType`](../../Foundation/nsuseractivity/activitytype.md) property to the name of the intent class that was handled. As with a custom user activity object, SiriKit fills the [`interaction`](../../Foundation/nsuseractivity/interaction.md) property of the object with the intent and your response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inintentresponse/useractivity)*