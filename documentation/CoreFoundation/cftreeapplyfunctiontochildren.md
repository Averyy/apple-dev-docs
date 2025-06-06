# CFTreeApplyFunctionToChildren(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Calls a function once for each immediate child of a tree.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFTreeApplyFunctionToChildren(_ tree: CFTree!, _ applier: ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void)!, _ context: UnsafeMutableRawPointer!)
```

#### Discussion

Note that the applier only operates one level deep—it does not operate on descendants further removed than the immediate children of a tree. If the tree is mutable, it is unsafe for the applied function to change the contents of the tree.

## Parameters

- `tree`: The tree to operate upon.
- `applier`: The callback function to call once for each child in  . The function must be able to apply to all the values in the tree.
- `context`: A pointer-sized program-defined value that is passed to the applier function, but is otherwise unused by this function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftreeapplyfunctiontochildren(_:_:_:))*