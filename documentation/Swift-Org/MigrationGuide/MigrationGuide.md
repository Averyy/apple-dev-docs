---
url: "https://docs.swift.org/latest/documentation/migrationguide"
framework: "Swift-Org/MigrationGuide"
---

# Migrating to Swift 6

**Framework**: Swift-Org/MigrationGuide

#### Overview

Swift’s concurrency system, introduced in [Swift 5.5](https://www.swift.org/blog/swift-5.5-released/), makes asynchronous and parallel code easier to write and understand. With the Swift 6 language mode, the compiler can now guarantee that concurrent programs are free of data races. When enabled, compiler safety checks that were previously optional become required.

Adopting the Swift 6 language mode is entirely under your control on a per-target basis. Targets that build with previous modes, as well as code in other languages exposed to Swift, can all interoperate with modules that have been migrated to the Swift 6 language mode.

It is possible you have been incrementally adopting concurrency features as they were introduced. Or, you may have been waiting for the Swift 6 release to begin using them. Regardless of where your project is in this process, this guide provides concepts and practical help to ease the migration.

You will find articles and code examples here that:

- Explain the concepts used by Swift’s data-race safety model.
- Outline a possible way to get started with migration.
- Show how to enable complete concurrency checking for Swift 5 projects.
- Demonstrate how to enable the Swift 6 language mode.
- Present strategies to resolve common problems.
- Provide techniques for incremental adoption.

> ❗ **Important**: The Swift 6 language mode is *opt-in*. Existing projects will not switch to this mode without configuration changes.
>
> There is a distinction between the *compiler version* and *language mode*. The Swift 6 compiler supports four distinct language modes: “6”, “5”, “4.2”, and “4”.

##### Contributing

This guide is under active development. You can view the source, see full code examples, and learn about how to contribute in the [repository](https://github.com/apple/swift-migration-guide). We would love your contributions in the form of:

- Filing [issues](https://github.com/apple/swift-migration-guide/issues) to cover specific code patterns or additional sections of the guide
- Opening pull requests to improve existing content or add new content
- Reviewing others’ [pull requests](https://github.com/apple/swift-migration-guide/pulls) for clarity and correctness of writing and code examples

For more information, see the [contributing](https://github.com/apple/swift-migration-guide/blob/main/CONTRIBUTING.md) document.

## Topics

- [Data Race Safety](../Swift-6-Concurrency-Migration-Guide/dataracesafety.md)
  Learn about the fundamental concepts Swift uses to enable data-race-free concurrent code.
- [Migration Strategy](../Swift-6-Concurrency-Migration-Guide/migrationstrategy.md)
  Get started migrating your project to the Swift 6 language mode.
- [Enable data-race safety checking](../Swift-6-Concurrency-Migration-Guide/enabledataracesafety.md)
  Use Swift 6 to get full data-race safety checking or add checking to an existing Swift 5 project.
- [Common Compiler Errors](../Swift-6-Concurrency-Migration-Guide/commonproblems.md)
  Identify, understand, and address common problems you can encounter while working with Swift concurrency.
- [Incremental Adoption](../Swift-6-Concurrency-Migration-Guide/incrementaladoption.md)
  Learn how you can introduce Swift concurrency features into your project incrementally.
- [Migrating to upcoming language features](../Swift-6-Concurrency-Migration-Guide/featuremigration.md)
  Migrate your project to upcoming language features.
- [Source Compatibility](../Swift-6-Concurrency-Migration-Guide/sourcecompatibility.md)
  See an overview of potential source compatibility issues.
- [Library Evolution](../Swift-6-Concurrency-Migration-Guide/libraryevolution.md)
  Annotate library APIs for concurrency while preserving source and ABI compatibility.
### Swift Concurrency in Depth
- [Runtime Behavior](../Swift-6-Concurrency-Migration-Guide/runtimebehavior.md)
  Learn how Swift concurrency runtime semantics differ from other runtimes you may be familiar with, and familiarize yourself with common patterns to achieve similar end results in terms of execution semantics.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/migrationguide)*