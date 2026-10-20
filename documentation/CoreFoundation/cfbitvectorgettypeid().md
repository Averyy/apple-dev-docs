# CFBitVectorGetTypeID()

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the type identifier for the CFBitVector opaque type.

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
func CFBitVectorGetTypeID() -> CFTypeID
```

```c
extern CFTypeID CFBitVectorGetTypeID();
```

#### Return Value

The type identifier for the CFBitVector opaque type.

#### Discussion

CFMutableBitVector objects have the same type identifier as CFBitVector objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbitvectorgettypeid())*