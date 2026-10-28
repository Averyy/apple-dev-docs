# isActive

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the region is active.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- macOS 27.1+
- tvOS 27.1+
- visionOS 27.1+
- watchOS 27.1+

## Declaration

```swift
var isActive: Bool { get }
```

## Discussion

A region can become active or inactive as conditions change. An active region currently affects your view. An inactive region doesn’t. For example, the fold of iPhone Duo is active when the device is partially open, and inactive when it’s fully open.

By default, [`reservedRegions(kind:options:layoutDirectionBehavior:)`](../geometryproxy/reservedregions%28kind,options,layoutdirectionbehavior%29.md) returns only active regions. To also get inactive regions, pass [`includeInactive`](./queryoptions/includeinactive.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/reservedregion/isactive)*