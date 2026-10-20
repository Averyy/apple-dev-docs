# CFBooleanGetValue(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the value of a CFBoolean object as a standard C type `Boolean`.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFBooleanGetValue(_ boolean: CFBoolean!) -> Bool
```

```c
extern Boolean CFBooleanGetValue(CFBooleanRef boolean);
```

#### Return Value

The value of `boolean`.

## Parameters

- `boolean`: The boolean to examine.

## See Also

### CFBoolean Miscellaneous Functions
- [func CFBooleanGetTypeID() -> CFTypeID](./cfbooleangettypeid%28%29.md)
  Returns the Core Foundation type identifier for the CFBoolean opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbooleangetvalue(_:))*