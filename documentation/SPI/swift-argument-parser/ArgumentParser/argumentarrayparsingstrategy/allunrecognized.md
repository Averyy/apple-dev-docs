---
url: "https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/argumentarrayparsingstrategy/allunrecognized"
framework: "swift-argument-parser/ArgumentParser"
---

# allUnrecognized

**Framework**: swift-argument-parser/ArgumentParser  
**Kind**: property  
**Role**: Type Property

After parsing, capture all unrecognized inputs in this argument array.

## Declaration

```swift
static var allUnrecognized: ArgumentArrayParsingStrategy { get }
```

#### Discussion

You can use the `allUnrecognized` parsing strategy to suppress “unexpected argument” errors or to capture unrecognized inputs for further processing.

For example, the `Example` command defined below has an `other` array that uses the `allUnrecognized` parsing strategy:

```
@main
struct Example: ParsableCommand {
    @Flag var verbose = false
    @Argument var name: String

    @Argument(parsing: .allUnrecognized)
    var other: [String]

    func run() {
        print(other.joined(separator: "\n"))
    }
}
```

After parsing the `--verbose` flag and `<name>` argument, any remaining input is captured in the `other` array.

```
$ example --verbose Negin one two
one
two
$ example Asa --verbose --other -zzz
--other
-zzz
```

## See Also

### Parsing Strategies
- [static var remaining: ArgumentArrayParsingStrategy](./remaining.md)
  Parse only unprefixed values from the command-line input, ignoring any inputs that have a dash prefix; this is the default strategy.
- [static var postTerminator: ArgumentArrayParsingStrategy](./postterminator.md)
  Before parsing arguments, capture all inputs that follow the `--` terminator in this argument array.
- [static var captureForPassthrough: ArgumentArrayParsingStrategy](./captureforpassthrough.md)
  Parse all remaining inputs after parsing any known options or flags, including dash-prefixed inputs and the `--` terminator.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-argument-parser/main/documentation/argumentparser/argumentarrayparsingstrategy/allunrecognized)*