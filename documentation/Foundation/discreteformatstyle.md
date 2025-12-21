# DiscreteFormatStyle

**Framework**: Foundation  
**Kind**: protocol

A format style that transforms a continuous input into a discrete output and provides information about its discretization boundaries.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
protocol DiscreteFormatStyle<FormatInput, FormatOutput> : FormatStyle
```

#### Overview

Use this protocol to keep displays up to date if input changes continuously, or to iterate over all possible outputs of a [`FormatStyle`](formatstyle.md) by obtaining the next discrete input in either direction from [`discreteInput(before:)`](discreteformatstyle/discreteinput(before:).md) or [`discreteInput(after:)`](discreteformatstyle/discreteinput(after:).md).

#### Ordering of Inputs

The ordering over [`FormatInput`](formatstyle/formatinput.md) defined by [`discreteInput(before:)`](discreteformatstyle/discreteinput(before:).md) / [`discreteInput(after:)`](discreteformatstyle/discreteinput(after:).md) must be consistent between the two functions. If [`FormatInput`](formatstyle/formatinput.md) conforms to the `Comparable` protocol, the format style’s ordering  be consistent with the canonical ordering defined via the `Comparable` conformance, i.e. it should hold that `discreteInput(before: x)! < x < discreteInput(after: x)!` where discrete inputs are not nil.

#### Stepping Through Discrete Inputoutput Pairs

One use case of this protocol is enumerating all discrete inputs of a format style and their respective outputs.

While the [`discreteInput(before:)`](discreteformatstyle/discreteinput(before:).md) and [`discreteInput(after:)`](discreteformatstyle/discreteinput(after:).md) functions are the right tool for that, they do not give a guarantee that their respective return values actually produce an output that is different from the output produced by formatting the `input` value used when calling [`discreteInput(before:)`](discreteformatstyle/discreteinput(before:).md) / [`discreteInput(after:)`](discreteformatstyle/discreteinput(after:).md), they only provide a value that produces a different output for  inputs. E.g. when formatting a floating point value as an integer, we can get the next discrete input after `x` by calculating `floor(x + 1)`. However, when rounding toward zero, the whole interval (-1;1) formats as zero. It would be ok for a discrete format style to ignore that edge case and return `0` for the [`discreteInput(after:)`](discreteformatstyle/discreteinput(after:).md) a negative value greater than `-1`. Therefore, to enumerate all discrete input/output pairs, adjacent outputs must be deduplicated in order to guarantee no adjacent outputs are the same.

The following example produces all discrete input/output pairs for inputs in a given `range` making sure adjacent outputs are unequal:

```swift
extension DiscreteFormatStyle
    where FormatInput : Comparable, FormatOutput : Equatable
{
        func enumerated(
        in range: ClosedRange<FormatInput>
    ) -> [(input: FormatInput, output: FormatOutput)] {
        var input = range.lowerBound
        var output = format(input)

        var pairs = [(input: FormatInput, output: FormatOutput)]()
        pairs.append((input, output))

        // get the next discretization bound
        while let nextInput = discreteInput(after: input),
              // check that it is still in the requested `range`
              nextInput <= range.upperBound {
            // get the respective formatted output
            let nextOutput = format(nextInput)
            // deduplicate based on the formatted output
            if nextOutput != output {
                pairs.append((nextInput, nextOutput))
            }
                input = nextInput
            output = nextOutput
        }

        return pairs
    }
}
```

#### Imperfect Discretization Boundaries

In some scenarios, a format style cannot provide precise discretization boundaries in a performant manner. In those cases it must override [`input(before:)`](discreteformatstyle/input(before:).md) and [`input(after:)`](discreteformatstyle/input(after:).md) to reflect that. For any discretization boundary `x` returned by either [`discreteInput(before:)`](discreteformatstyle/discreteinput(before:).md) or [`discreteInput(after:)`](discreteformatstyle/discreteinput(after:).md) based on the original input `y`, all values representable in the [`FormatInput`](formatstyle/formatinput.md)strictly  between `x` and the return value of `input(after: x)` or `input(before: x)`, respectively, are not guaranteed to produce the same formatted output as `y`.

The following schematic shows an overview of the guarantees given by the protocol:

```None
xB = discreteInput(before: y)       y      xA = discreteInput(after: y)
      |                             |                             |
<-----+---+-------------------------+-------------------------+---+--->
          |                                                   |
 zB = input(after: xB)                          zA = input(before: xA)
```

- the formatted output for everything in `zB...zA` (including bounds) is  to be equal to `format(y)`
- the formatted output for `xB` and lower is  different from `format(y)`
- the formatted output for `xA` and higher is  different from `format(y)`
- the  formatted output between `xB` and `zB`, as well as `zA` and `xA` (excluding bounds) cannot be predicted

## Topics

### Instance Methods
- [func discreteInput(after: Self.FormatInput) -> Self.FormatInput?](discreteformatstyle/discreteinput(after:).md)
  The next discretization boundary after the given input.
- [func discreteInput(before: Self.FormatInput) -> Self.FormatInput?](discreteformatstyle/discreteinput(before:).md)
  The next discretization boundary before the given input.
- [func input(after: Self.FormatInput) -> Self.FormatInput?](discreteformatstyle/input(after:).md)
  The next input value after the given input.
- [func input(before: Self.FormatInput) -> Self.FormatInput?](discreteformatstyle/input(before:).md)
  The next input value before the given input.

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [FormatStyle](formatstyle.md)
- [Hashable](../Swift/Hashable.md)
### Conforming Types
- [Date.AnchoredRelativeFormatStyle](date/anchoredrelativeformatstyle.md)
- [Date.ComponentsFormatStyle](date/componentsformatstyle.md)
- [Date.FormatStyle](date/formatstyle.md)
- [Date.FormatStyle.Attributed](date/formatstyle/attributed-swift.struct.md)
- [Date.VerbatimFormatStyle](date/verbatimformatstyle.md)
- [Date.VerbatimFormatStyle.Attributed](date/verbatimformatstyle/attributed-swift.struct.md)

## See Also

- [protocol NSKeyValueObservingCustomization](nskeyvalueobservingcustomization.md)
  Conforming to NSKeyValueObservingCustomization is not required to use Key-Value Observing. Provide an implementation of these functions if you need to disable auto-notifying for a key, or add dependent keys


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/discreteformatstyle)*