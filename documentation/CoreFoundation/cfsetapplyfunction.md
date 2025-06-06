# CFSetApplyFunction(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Calls a function once for each value in a set.

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
func CFSetApplyFunction(_ theSet: CFSet!, _ applier: ((UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void)!, _ context: UnsafeMutableRawPointer!)
```

#### Discussion

If `theSet` is mutable, it is unsafe for the `applier` function to change the contents of the collection.

## Parameters

- `theSet`: The set to operate upon.
- `applier`: The callback function to call once for each value in the  . If this parameter is not a pointer to a function of the correct prototype, the behavior is undefined. The   function must be able to work with all values in  .
- `context`: A pointer-sized program-defined value, which is passed as the second parameter to the   function, but is otherwise unused by this function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsetapplyfunction(_:_:_:))*