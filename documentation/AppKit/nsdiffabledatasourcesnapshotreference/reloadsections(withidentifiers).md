# reloadSections(withIdentifiers:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Reloads the data within the specified sections of the snapshot.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func reloadSections(withIdentifiers sectionIdentifiers: [Any])
```

```objc
- (void) reloadSectionsWithIdentifiers:(NSArray<id> *) sectionIdentifiers;
```

## Parameters

- `sectionIdentifiers`: The array of identifiers corresponding to the sections to reload in the snapshot.

## See Also

### Reloading data
- [func reloadItems(withIdentifiers: [Any])](./reloaditems%28withidentifiers%29.md)
  Reloads the data within the specified items in the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshotreference/reloadsections(withidentifiers:))*