# CFShowStr(_:)

**Framework**: Core Foundation  
**Kind**: func

Prints the attributes of a string during debugging.

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
func CFShowStr(_ str: CFString!)
```

#### Discussion

Use this function to learn about specific attributes of a CFString object during debugging. These attributes include the following:

- Length (in Unicode characters)
- Whether originally it was an 8-bit string and, if so, whether it was a C (`HasNullByte`) or Pascal (`HasLengthByte`) string
- Whether it is a mutable or an immutable object
- The allocator used to create it
- The memory address of the character contents and whether those contents are in-line

The information provided by this function is for debugging purposes only. The values of any of these attributes might change between different releases and on different platforms. Note in particular that this function does not show the contents of the string. If you want to display the contents of the string, use [`CFShow(_:)`](cfshow(_:).md).

##### Special Considerations

You can use `CFShowStr` in one of two general ways. If your debugger supports function calls (such as `gdb` does), call `CFShowStr` in the debugger:

```objc
(gdb) call (void) CFShowStr(string)
Length 11
IsEightBit 1
HasLengthByte 1
HasNullByte 1
InlineContents 1
Allocator SystemDefault
Mutable 0
Contents 0x4e7c0
```

You can also incorporate calls to `CFShowStr` in a test version of your code to print descriptions of CFString objects to the console.

## Parameters

- `str`: The string whose attributes you want to print.

## See Also

- [func CFStringGetTypeID() -> CFTypeID](cfstringgettypeid().md)
  Returns the type identifier for the CFString opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfshowstr(_:))*