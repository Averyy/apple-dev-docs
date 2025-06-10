# joined(separator:)

**Framework**: Swift  
**Kind**: method

Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func joined(separator: String = "") -> String
```

#### Return Value

A single, concatenated string.

#### Discussion

The following example shows how an array of strings can be joined to a single, comma-separated string:

```swift
let cast = ["Vivien", "Marlon", "Kim", "Karl"]
let list = cast.joined(separator: ", ")
print(list)
// Prints "Vivien, Marlon, Kim, Karl"
```

## Parameters

- `separator`: A string to insert between each of the elements   in this sequence. The default separator is an empty string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/joined(separator:)-2rxv1)*