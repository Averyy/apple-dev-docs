---
url: "https://docs.swift.org/latest/documentation/cxx/cxxuniqueset/insert(_:)"
framework: "Swift-Org/Cxx"
---

# insert(_:)

**Framework**: Swift-Org/Cxx  
**Kind**: method  
**Role**: Instance Method

Inserts the given element in the set if it is not already present.

## Declaration

```swift
@discardableResult
mutating func insert(_ newMember: Element) -> (inserted: Bool, memberAfterInsert: Element)
```

## Return Value

`(true, newMember)` if `newMember` was not contained in the set. If an element equal to `newMember` was already contained in the set, the method returns `(false, oldMember)`, where `oldMember` is the element that was equal to `newMember`.

## Discussion

If an element equal to `newMember` is already contained in the set, this method has no effect.

## Parameters

- `newMember`: An element to insert into the set.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/cxx/cxxuniqueset/insert(_:))*