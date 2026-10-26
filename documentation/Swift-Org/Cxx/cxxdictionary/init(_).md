---
url: "https://docs.swift.org/latest/documentation/cxx/cxxdictionary/init(_:)"
framework: "Swift-Org/Cxx"
---

# init(_:)

**Framework**: Swift-Org/Cxx  
**Kind**: init  
**Role**: Initializer

Creates a C++ map containing the elements of a Swift Dictionary.

## Declaration

```swift
init(_ dictionary: Dictionary<Key, Value>) where Self.Key : Hashable
```

#### Discussion

This initializes the map by copying every key and value of the dictionary.

> **Complexity**: O(*n*), where *n* is the number of entries in the Swift dictionary


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxdictionary/init(_:))*