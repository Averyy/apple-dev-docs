# CFStringGetTypeID()

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the type identifier for the CFString opaque type.

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
func CFStringGetTypeID() -> CFTypeID
```

```c
extern CFTypeID CFStringGetTypeID();
```

## Return Value

The type identifier for the CFString opaque type.

## Discussion

CFMutableString objects have the same type identifier as CFString objects.

## See Also

### Getting String Properties
- [func CFShowStr(CFString!)](./cfshowstr%28_%29.md)
  Prints the attributes of a string during debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringgettypeid())*