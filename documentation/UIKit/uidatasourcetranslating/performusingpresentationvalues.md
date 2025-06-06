# performUsingPresentationValues(_:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Performs actions on the current object using index paths that are relative to the presentation layer of that object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func performUsingPresentationValues(_ actionsToTranslate: () -> Void)
```

#### Discussion

Use this method to perform actions on the current object, when the index paths for those actions are relative to the object’s presentation layer. For example, you might call this method to modify a table view or collection view that has uncommitted updates.

## Parameters

- `actionsToTranslate`: A block containing the code you want to execute. Any index paths you specify in this block must be relative to the presentation layer of the object (instead of relative to its data source object). This block takes no parameters and has no return value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatasourcetranslating/performusingpresentationvalues(_:))*