# appEntityIdentifier

**Framework**: Foundation  
**Kind**: property

The identifier of an app entity that you associate with the user activity.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
var appEntityIdentifier: EntityIdentifier? { get set }
```

#### Discussion

By associating an app entity with a user activity, you make the entity available to Siri and Apple Intelligence. To clear the association with the app entity, set `appEntityIdentifier` to `nil`.

For more information, refer to [`Making onscreen content available to Siri and Apple Intelligence`](https://developer.apple.com/documentation/AppIntents/Making-onscreen-content-available-to-siri-and-apple-intelligence) and [`App Intents`](https://developer.apple.com/documentation/AppIntents).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/appentityidentifier)*