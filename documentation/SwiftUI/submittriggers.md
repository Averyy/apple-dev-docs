# SubmitTriggers

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A type that defines various triggers that result in the firing of a submission action.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct SubmitTriggers
```

## Overview

These triggers may be provided to the [`onSubmit(of:_:)`](./view/onsubmit%28of,_%29.md) modifier to alter which types of user behaviors trigger a provided submission action.

## Topics

### Getting submit triggers
- [static let search: SubmitTriggers](./submittriggers/search.md)
  Defines triggers originating from search fields constructed from searchable modifiers.
- [static let text: SubmitTriggers](./submittriggers/text.md)
  Defines triggers originating from text input controls like `TextField` and `SecureField`.
### Creating a set of options
- [init(rawValue: SubmitTriggers.RawValue)](./submittriggers/init%28rawvalue%29.md)
  Creates a set of submit triggers.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Responding to submission events
- [func onSubmit(of: SubmitTriggers, () -> Void) -> some View](./view/onsubmit%28of,_%29.md)
  Adds an action to perform when the user submits a value to this view.
- [func submitScope(Bool) -> some View](./view/submitscope%28_%29.md)
  Prevents submission triggers originating from this view to invoke a submission action configured by a submission modifier higher up in the view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/submittriggers)*