# scanForNetworks(withName:)

**Framework**: Corewlan  
**Kind**: method

Scans for networks.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func scanForNetworks(withName networkName: String?) throws -> Set<CWNetwork>
```

#### Return Value

A set of CWNetwork objects.

#### Discussion

If  parameter is present, a directed scan will be performed by the interface, otherwise a broadcast scan will be performed. This method will block for the duration of the scan.

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `networkName`: The name (SSID) of the network for which to scan.

## See Also

- [func scanForNetworks(withSSID: Data?) throws -> Set<CWNetwork>](cwinterface/scanfornetworks(withssid:).md)
  Scans for networks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwinterface/scanfornetworks(withname:))*