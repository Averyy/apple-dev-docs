# appEntityIdentifier

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

The identifier of an app entity you set on framework types to make app content available to system experiences.

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

Set this property to `nil` to clear the association between your [`AppEntity`](appentity.md) and the system type that adopts [`AppEntityAnnotatable`](appentityannotatable.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appentityannotatable/appentityidentifier)*