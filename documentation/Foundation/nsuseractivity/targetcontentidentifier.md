# targetContentIdentifier

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A string that identifies the user activity’s content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var targetContentIdentifier: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSString * targetContentIdentifier;
```

*macOS*

```objc
@property (copy, nullable) NSString * targetContentIdentifier;
```

## Mentions

- [Supporting the creation of Quick Notes](../supporting-the-creation-of-quick-notes.md)

## Discussion

A target content identifier is a string you define within your app. This string provides a unique identifier for specific content in your app, like a particular document or the location of a piece of data in a database. This string isn’t visible to the user.

If you set this property, when the system delivers an [`NSUserActivity`](../nsuseractivity.md) object to an app with multiple scenes, it chooses the [`UIScene`](../../UIKit/uiscene.md) whose [`UISceneActivationConditions`](../../UIKit/uisceneactivationconditions.md) have the best match with the target content identifier. For more information, see [`UISceneActivationConditions`](../../UIKit/uisceneactivationconditions.md).

This property is optional but is highly recommended to create a great multitasking experience for apps that run on iPad. Setting this property doesn’t automatically set [`needsSave`](./needssave.md) to [`true`](../../Swift/true.md).

## See Also

### Specifying app identifiers
- [var appEntityIdentifier: EntityIdentifier?](./appentityidentifier.md)
  The identifier of an app entity that you associate with the user activity.
- [var externalMediaContentIdentifier: String?](./externalmediacontentidentifier.md)
  A unique identifier from the app’s media content catalog for the currently displayed media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/targetcontentidentifier)*