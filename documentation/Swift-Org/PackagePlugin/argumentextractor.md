---
url: "https://docs.swift.org/latest/documentation/packageplugin/argumentextractor"
framework: "Swift-Org/PackagePlugin"
---

# ArgumentExtractor

**Framework**: Swift-Org/PackagePlugin  
**Kind**: struct  
**Role**: Structure

A rudimentary helper for extracting options and flags from a list of strings that represent command line arguments.

## Declaration

```swift
struct ArgumentExtractor
```

#### Overview

Create the extractor with the full command line arguments provided, then extract all known options and flags, which leaves the positional arguments.

This does not handle the case where positional arguments (or optional argument values) have the same name as an option or a flag. It only handles the long form of options, not short forms, for example: `--<name>`, not `-n`. It respects an argument that consists of two hyphens (`--`) as an indication that all remaining arguments are positional.

## Topics

### Creating an Argument Extractor
- [init([String])](./argumentextractor/init%28_%29.md)
  Creates an argument extractor with a list of strings from which to extract flags and options.
### Inspecting Arguments
- [var remainingArguments: [String]](./argumentextractor/remainingarguments.md)
  Returns all remaining arguments.
- [var unextractedOptionsOrFlags: [String]](./argumentextractor/unextractedoptionsorflags.md)
  Returns any unextracted flags or options.
### Extracting Arguments
- [func extractFlag(named: String) -> Int](./argumentextractor/extractflag%28named%29.md)
  Extracts flags of the form `--<name>` from the remaining arguments, and returns the count.
- [func extractOption(named: String) -> [String]](./argumentextractor/extractoption%28named%29.md)
  Extracts options of the form `--<name> <value>` or `--<name>=<value>` from the remaining arguments and returns the extracted values.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/argumentextractor)*