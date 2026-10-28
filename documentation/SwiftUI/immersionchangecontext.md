# ImmersionChangeContext

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A structure that represents a state of immersion of your app.

**Availability**:
- macOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct ImmersionChangeContext
```

## Overview

You don’t use this structure directly. Instead, SwiftUI provides instances of this structure via the `onImmersionChange` modifier’s closure.

## Topics

### Instance Properties
- [let amount: Double?](./immersionchangecontext/amount.md)
  The current amount of immersion.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Responding to immersion changes
- [func onImmersionChange(initial: Bool, (ImmersionChangeContext, ImmersionChangeContext) -> Void) -> some View](./view/onimmersionchange%28initial,_%29.md)
  Performs an action when the immersion state of your app changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersionchangecontext)*