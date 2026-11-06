# entities

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

The entities to delete: the elements of [`target`](./target-1cesv.md).

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
var entities: [Self.Entity] { get }
```

Available when `Entity` is `Self.Target.Element`, `Target` conforms to `Sequence`, and `Target.Element` is `Self.Target.ValueType`.

## Discussion

When `target` is a set, the order of the entities is unspecified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/deleteintent/entities-5etox)*