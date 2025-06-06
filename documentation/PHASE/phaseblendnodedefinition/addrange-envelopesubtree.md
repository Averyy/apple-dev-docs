# addRange(envelope:subtree:)

**Framework**: PHASE  
**Kind**: method

Adds a child node with an envelope.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func addRange(envelope: PHASEEnvelope, subtree: PHASESoundEventNodeDefinition)
```

## Parameters

- `envelope`: A shaped audio signal over a range.
- `subtree`: A child node that’s active in the blend range an envelope defines.

## See Also

- [func addRangeForInputValuesAbove(value: Double, fullGainAtValue: Double, fadeCurveType: PHASECurveType, subtree: PHASESoundEventNodeDefinition)](phaseblendnodedefinition/addrangeforinputvaluesabove(value:fullgainatvalue:fadecurvetype:subtree:).md)
  Adds a child node that blends above a given value.
- [func addRangeForInputValuesBelow(value: Double, fullGainAtValue: Double, fadeCurveType: PHASECurveType, subtree: PHASESoundEventNodeDefinition)](phaseblendnodedefinition/addrangeforinputvaluesbelow(value:fullgainatvalue:fadecurvetype:subtree:).md)
  Adds a child node that blends below a given value.
- [func addRangeForInputValuesBetween(lowValue: Double, highValue: Double, fullGainAtLowValue: Double, fullGainAtHighValue: Double, lowFadeCurveType: PHASECurveType, highFadeCurveType: PHASECurveType, subtree: PHASESoundEventNodeDefinition)](phaseblendnodedefinition/addrangeforinputvaluesbetween(lowvalue:highvalue:fullgainatlowvalue:fullgainathighvalue:lowfadecurvetype:highfadecurvetype:subtree:).md)
  Adds a child node that blends between a given high and low value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseblendnodedefinition/addrange(envelope:subtree:))*