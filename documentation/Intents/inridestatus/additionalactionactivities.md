# additionalActionActivities

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

Additional activities that the user may choose to perform while the ride request is active.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var additionalActionActivities: [NSUserActivity]? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSArray<NSUserActivity *> * additionalActionActivities;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSArray<NSUserActivity *> * additionalActionActivities;
```

## Discussion

If there are actions related to the ride that the user can take in your app, create user activity objects for each one and assign them to this property. For example, you might include actions to share the estimated arrival time with another user, split the fare with someone, or pay for the ride immediately. When you specify one or more actions, Maps displays buttons for each action. (Siri does not use this property). The [`title`](../../Foundation/nsuseractivity/title.md) property of the corresponding [`NSUserActivity`](../../Foundation/nsuseractivity.md) object provides the title of each button. If the user selects an action, Maps launches your app and passes the selected user activity object to it for handling.

## See Also

### Providing User Activity Objects
- [var userActivityForCancelingInApplication: NSUserActivity?](./useractivityforcancelinginapplication.md)
  A user activity object for canceling the ride request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridestatus/additionalactionactivities)*