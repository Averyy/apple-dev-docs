# appEntityIdentifier

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

The identifier of an app entity you want to associate with a system type.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst ?+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
var appEntityIdentifier: EntityIdentifier? { get set }
```

## Mentions

- [Providing contextual cues to Apple Intelligence and Siri](providing-contextual-cues-to-apple-intelligence-and-siri.md)
- [Donating your app’s data and actions to the system](donating-your-apps-data-and-actions-to-the-system.md)

#### Discussion

This property stores the unique identifier of one of your app’s entities. Use it to create an association between a system type and one of your custom [`AppEntity`](appentity.md) types. For example, the [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) makes this property available so you can specify the entity associated with your app’s activity. To remove the association with one of your app’s entities, set this property to `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appentityannotatable/appentityidentifier)*