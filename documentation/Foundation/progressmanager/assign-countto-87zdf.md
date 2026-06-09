# assign(count:to:)

**Framework**: Foundation  
**Kind**: method

Adds a Foundation’s `Progress` instance as a child which constitutes a certain `count` of `self`’s `totalCount`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
final func assign(count: Int, to progress: Progress)
```

## Parameters

- `count`: Number of units delegated from `self`’s `totalCount`.
- `progress`: `Progress` which receives the delegated `count`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/progressmanager/assign(count:to:)-87zdf)*