# CFDictionaryApplyFunction(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Calls a function once for each key-value pair in a dictionary.

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
func CFDictionaryApplyFunction(_ theDict: CFDictionary!, _ applier: ((UnsafeRawPointer?, UnsafeRawPointer?, UnsafeMutableRawPointer?) -> Void)!, _ context: UnsafeMutableRawPointer!)
```

#### Discussion

If this function iterates over a mutable collection, it is unsafe for the `applier` function to change the contents of the collection.

## Parameters

- `theDict`: The dictionary to operate upon.
- `applier`: The callback function to call once for each key-value pair in  . If this parameter is not a pointer to a function of the correct prototype, the behavior is undefined. If there are keys or values which the   function does not expect or cannot properly apply to, the behavior is undefined.
- `context`: A pointer-sized program-defined value, which is passed as the third parameter to the applier function, but is otherwise unused by this function. The value must be appropriate for the   function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionaryapplyfunction(_:_:_:))*