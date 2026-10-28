# CFDataGetTypeID()

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the type identifier for the CFData opaque type.

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
func CFDataGetTypeID() -> CFTypeID
```

```c
extern CFTypeID CFDataGetTypeID();
```

## Return Value

The type identifier for the CFData opaque type.

## Discussion

CFMutableData objects have the same type identifier as CFData objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdatagettypeid())*