# Subprogress

**Framework**: Foundation  
**Kind**: struct

Subprogress is used to establish parent-child relationship between two instances of `ProgressManager`.

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
struct Subprogress
```

#### Overview

Subprogress is returned from a call to `subprogress(assigningCount:)` by a parent ProgressManager. A child ProgressManager is then returned by calling `start(totalCount:)` on a Subprogress.

## Topics

### Instance Methods
- [func start(totalCount: Int?) -> ProgressManager](subprogress/start(totalcount:).md)
  Instantiates a ProgressManager which is a child to the parent from which `self` is returned.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/subprogress)*