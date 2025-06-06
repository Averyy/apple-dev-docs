# lastIndex(of:)

**Framework**: System  
**Kind**: method

Returns the last index where the specified value appears in the collection.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func lastIndex(of element: Self.Element) -> Self.Index?
```

#### Return Value

The last index where `element` is found. If `element` is not found in the collection, this method returns `nil`.

#### Discussion

After using `lastIndex(of:)` to find the position of the last instance of a particular element in a collection, you can use it to access the element by subscripting. This example shows how you can modify one of the names in an array of students.

```swift
var students = ["Ben", "Ivy", "Jordell", "Ben", "Maxime"]
if let i = students.lastIndex(of: "Ben") {
    students[i] = "Benjamin"
}
print(students)
// Prints "["Ben", "Ivy", "Jordell", "Benjamin", "Max"]"
```

> **Note**: O(), where  is the length of the collection.

## Parameters

- `element`: An element to search for in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/componentview/lastindex(of:))*