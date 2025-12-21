# updateTitle(_:subtitle:)

**Framework**: Background Tasks  
**Kind**: method

Update the task title and subtitle that the system displays to a person.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
func updateTitle(_ title: String, subtitle: String)
```

#### Discussion

The system displays Continuous Background Task requests in a Live Activity for a person to monitor progress and cancel a task, if they wish.

## Parameters

- `title`: The localized title displayed to a person.
- `subtitle`: The localized subtitle displayed to a person.

## See Also

- [var title: String](bgcontinuedprocessingtask/title.md)
  The localized title displayed to a person.
- [var subtitle: String](bgcontinuedprocessingtask/subtitle.md)
  The localized subtitle displayed to a person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtask/updatetitle(_:subtitle:))*