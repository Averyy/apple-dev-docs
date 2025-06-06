# kLSMMapDiscardCounts

**Framework**: Latent Semantic Mapping  
**Kind**: var

An option that specifies not to keep counts.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var kLSMMapDiscardCounts: Int { get }
```

#### Discussion

If you specify this option when loading the map, you must reload the map without this option before calling [`LSMMapStartTraining(_:)`](lsmmapstarttraining(_:).md).

If you specify this option when storing the map, the stored map can’t be retrained at all. This option can save a lot of memory or disk space.

## See Also

- [var kLSMMapLoadMutable: Int](klsmmaploadmutable.md)
  An option that specifies to load the map as mutable in training state.
- [var kLSMMapHashText: Int](klsmmaphashtext.md)
  An option that specifies to transform the text so it’s not human-readable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/latentsemanticmapping/klsmmapdiscardcounts)*