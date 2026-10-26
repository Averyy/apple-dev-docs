---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loggingbestpractices"
framework: "swift-log/Logging"
---

# Logging best practices

**Framework**: swift-log/Logging

Best practices for effective logging with SwiftLog.

#### Overview

This collection of best practices helps library authors and application developers create effective, maintainable logging that works well across diverse environments. Each practice is designed to ensure your logs are useful for debugging while being respectful of system resources and operational requirements.

##### Who Should Use These Practices

- **Library Authors**: Creating reusable components that log appropriately.
- **Application Developers**: Implementing logging strategies in applications.

##### Philosophy

Good logging strikes a balance between providing useful information and avoiding system overhead. These practices are based on real-world experience with production systems and emphasize:

- **Predictable behavior** across different environments.
- **Performance consciousness** to avoid impacting application speed.
- **Operational awareness** to support production debugging and monitoring.
- **Developer experience** to make debugging efficient and pleasant.

##### Contributing to these practices

These best practices evolve based on community experience and are maintained by the Swift Server Working Group ([SSWG](https://www.swift.org/sswg/)). Each practice includes:

- **Clear motivation** explaining why the practice matters
- **Concrete examples** showing good and bad patterns
- **Alternatives considered** documenting trade-offs and rejected approaches

## Topics

- [001: Choosing log levels](./api-001-choosingloglevels.md)
  Select appropriate log levels in applications and libraries.
- [002: Structured logging](./api-002-structuredlogging.md)
  Use metadata to create machine-readable, searchable log entries.
- [003: Logger propagation in libraries](./api-003-acceptingloggers.md)
  Propagate caller context by accepting a `Logger` parameter or reading the task-local [`current`](./logger/current.md) — never by constructing your own logger.
- [004: Testing code that logs](./api-004-testinglogging.md)
  Validate what you code logs by capturing entries in memory rather than bootstrapping a process-wide backend.

## See Also

### Best Practices
- [Implementing a log handler](./implementingaloghandler.md)
  Create a custom logging backend that provides logging services for your apps and libraries.
- [Disable log levels during compilation](./disableloglevelsduringcompilation.md)
  SwiftLog provides compile-time traits to eliminate less severe log levels from your binary reducing the runtime overhead.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loggingbestpractices)*