# Subprogress

**Framework**: Foundation  
**Kind**: struct

Subprogress is used to establish parent-child relationship between two instances of `ProgressManager`.

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
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/subprogress)*