# GCInputArcadeButtonName

**Framework**: Game Controller  
**Kind**: func  
**Role**: Function

Returns the name of the arcade stick button at the specified location.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```c
extern GCInputButtonNameGCInputArcadeButtonName(NSInteger row, NSInteger column);
```

## Return Value

The name of an arcade stick button.

## Parameters

- `row`: The row on the arcade stick that the button appears in, where `0` is the bottom row.
- `column`: The column on the arcade stick that the button appears in, where `0` is the column nearest to the lever or direction buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcinputarcadebuttonname)*