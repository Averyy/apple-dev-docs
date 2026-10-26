---
url: "https://docs.swift.org/latest/documentation/packageplugin/pathlist/sorted(using:)-949oc"
framework: "Swift-Org/PackagePlugin"
---

# sorted(using:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: method  
**Role**: Instance Method

Inherited from `Sequence.sorted(using:)`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
func sorted<Comparator>(using comparator: Comparator) -> [Self.Element] where Comparator : SortComparator, Self.Element == Comparator.Compared
```


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/pathlist/sorted(using:)-949oc)*