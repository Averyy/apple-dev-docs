---
url: "https://docs.swift.org/latest/documentation/docc/column"
framework: "Swift-Org/docc"
---

# Column

**Framework**: Swift-Org/docc  
**Kind**: class  
**Role**: Directive

A container directive that holds general markup content describing a column with a row in a grid-based layout.

**Availability**:
- Swift-DocC 5.8+

## Declaration

```swift
@Column(size: Int = 1) {
    ...
}
```

## Overview

Create a column inside a [`Row`](./row.md) by nesting a `@Column` directive within the content for an `@Row` directive.

## Parameters

- `size`: The size of this column. **(optional)**

  Specify a value greater than `1` to make this column span multiple columns in the parent [`Row`](./row.md).


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/docc/column)*