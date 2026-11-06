# target

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

The entities to delete.

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
var target: Self.Target { get }
```

## Discussion

The default implementation returns [`entities`](./entities.md). It requires `Target` to be `[Entity]`, which is the default; an intent that declares a different `Target` must implement `target`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/deleteintent/target-5b0ss)*