# title

**Framework**: Background Tasks  
**Kind**: property

The localized title displayed to a person.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
var title: String { get }
```

#### Discussion

Define the value of this property as a parameter to the request initializer:  [`init(identifier:title:subtitle:)`](bgcontinuedprocessingtaskrequest/init(identifier:title:subtitle:).md). After that, this property is read only, however you can update the title by calling [`updateTitle(_:subtitle:)`](bgcontinuedprocessingtask/updatetitle(_:subtitle:).md).

## See Also

- [var subtitle: String](bgcontinuedprocessingtask/subtitle.md)
  The localized subtitle displayed to a person.
- [func updateTitle(String, subtitle: String)](bgcontinuedprocessingtask/updatetitle(_:subtitle:).md)
  Update the task title and subtitle that the system displays to a person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtask/title)*