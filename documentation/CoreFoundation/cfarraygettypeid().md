# CFArrayGetTypeID()

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the type identifier for the CFArray opaque type.

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
func CFArrayGetTypeID() -> CFTypeID
```

```c
extern CFTypeID CFArrayGetTypeID();
```

## Return Value

The type identifier for the CFArray opaque type.

## Discussion

CFMutableArray objects have the same type identifier as CFArray objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfarraygettypeid())*