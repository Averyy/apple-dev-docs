# CFAttributedStringGetTypeID()

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the type identifier for the CFAttributedString opaque type.

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
func CFAttributedStringGetTypeID() -> CFTypeID
```

```c
extern CFTypeID CFAttributedStringGetTypeID();
```

## Return Value

The type identifier for the CFAttributedString opaque type.

## Discussion

CFMutableAttributedString objects have the same type identifier as CFAttributedString objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfattributedstringgettypeid())*