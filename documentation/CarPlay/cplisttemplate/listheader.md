# listHeader

**Framework**: CarPlay  
**Kind**: property

An optional details header displayed at the top of the list template.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
var listHeader: CPListTemplateDetailsHeader? { get set }
```

#### Discussion

The list header provides a way to display additional context or summary information above the list sections. When set, the header appears between the navigation bar and the first list section.

Assigning to this property will dynamically update the List Template to show or hide the header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplate/listheader)*