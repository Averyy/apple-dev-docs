# assign(count:to:)

**Framework**: Foundation  
**Kind**: method

Adds a Foundation’s `Progress` instance as a child which constitutes a certain `count` of `self`’s `totalCount`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
final func assign(count: Int, to progress: Progress)
```

## Parameters

- `count`: Number of units delegated from `self`’s `totalCount`.
- `progress`: `Progress` which receives the delegated `count`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressmanager/assign(count:to:)-87zdf)*