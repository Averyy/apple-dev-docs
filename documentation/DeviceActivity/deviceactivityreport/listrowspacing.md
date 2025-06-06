# listRowSpacing(_:)

**Framework**: DeviceActivity  
**Kind**: method

Sets the vertical spacing between two adjacent rows in a List.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
nonisolated
func listRowSpacing(_ spacing: CGFloat?) -> some View
```

#### Discussion

The following example creates a List with 10 pts of spacing between each row:

```swift
List {
    Text("Blue")
    Text("Red")
}
.listRowSpacing(10.0)
```

## Parameters

- `spacing`: The spacing value to use. A value of   uses   the default spacing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreport/listrowspacing(_:))*