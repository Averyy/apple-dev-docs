# SubmitLabel

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A semantic label describing the label of submission within a view hierarchy.

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
struct SubmitLabel
```

## Overview

A submit label is a description of a submission action provided to a view hierarchy using the [`onSubmit(of:_:)`](./view/onsubmit%28of,_%29.md) modifier.

## Topics

### Getting submission labels
- [static var `continue`: SubmitLabel](./submitlabel/continue.md)
  Defines a submit label with text of “Continue”.
- [static var done: SubmitLabel](./submitlabel/done.md)
  Defines a submit label with text of “Done”.
- [static var go: SubmitLabel](./submitlabel/go.md)
  Defines a submit label with text of “Go”.
- [static var join: SubmitLabel](./submitlabel/join.md)
  Defines a submit label with text of “Join”.
- [static var next: SubmitLabel](./submitlabel/next.md)
  Defines a submit label with text of “Next”.
- [static var `return`: SubmitLabel](./submitlabel/return.md)
  Defines a submit label with text of “Return”.
- [static var route: SubmitLabel](./submitlabel/route.md)
  Defines a submit label with text of “Route”.
- [static var search: SubmitLabel](./submitlabel/search.md)
  Defines a submit label with text of “Search”.
- [static var send: SubmitLabel](./submitlabel/send.md)
  Defines a submit label with text of “Send”.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Labeling a submission event
- [func submitLabel(SubmitLabel) -> some View](./view/submitlabel%28_%29.md)
  Sets the submit label for this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/submitlabel)*