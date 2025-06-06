# state

**Framework**: Accelerate  
**Kind**: property

The state of the random number generator.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
var state: BNNS.RandomGeneratorState { get set }
```

#### Discussion

Use the random number generator’s [`state`](bnns/randomgenerator/state.md) property to save and restore the generator.

The following code creates a random number generator and captures its initial state. The code calls [`allocate(randomUniformUsing:range:shape:batchSize:)`](bnnsndarraydescriptor/allocate(randomuniformusing:range:shape:batchsize:)-761hg.md) twice to populate the arrays `a` and `b` with different random values. Before allocating the array `c` with random values, the code resets the generator’s state to create identical random values in arrays `a` and `c`.

```swift
guard
    let randomGenerator = BNNS.RandomGenerator(
        method: .aesCtr,
        seed: 1234) else {
        return
    }

let state = randomGenerator.state

let a = BNNSNDArrayDescriptor.allocate(
    randomUniformUsing: randomGenerator,
    range: Int16(-10)...Int16(10),
    shape: [16])!.makeArray(of: Int16.self)!

let b = BNNSNDArrayDescriptor.allocate(
    randomUniformUsing: randomGenerator,
    range: Int16(-10)...Int16(10),
    shape: [16])!.makeArray(of: Int16.self)!

// Prints "false".
print(a.elementsEqual(b))

randomGenerator.state = state

let c = BNNSNDArrayDescriptor.allocate(
    randomUniformUsing: randomGenerator,
    range: Int16(-10)...Int16(10),
    shape: [16])!.makeArray(of: Int16.self)!

// Prints "true".
print(a.elementsEqual(c))
```

## See Also

- [class RandomGeneratorState](bnns/randomgeneratorstate.md)
  An opaque object that contains the state of a random number generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/randomgenerator/state)*