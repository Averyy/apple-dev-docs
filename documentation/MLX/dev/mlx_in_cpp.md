---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/dev/mlx_in_cpp.html
---

# Using MLX in C++

**

- [.rst](../_sources/dev/mlx_in_cpp.rst)
- **

.pdf

**

# Using MLX in C++

 Table of contents 

# Using MLX in C++

You can use MLX in a C++ project with CMake.

Note

This guide is based one the following [example using MLX in C++](https://github.com/ml-explore/mlx/tree/main/examples/cmake_project)

First install MLX:

```
pip install -U mlx
```

You can also install the MLX Python package from source or just the C++
library. For more information see the [documentation on installing MLX](../install.html#build-and-install).

Next make an example program in `example.cpp`:

```
#include <iostream>

#include "mlx/mlx.h"

namespace mx = mlx::core;

int main() {
  auto x = mx::array({1, 2, 3});
  auto y = mx::array({1, 2, 3});
  std::cout << x + y << std::endl;
  return 0;
}
```

The next step is to setup a CMake file in `CMakeLists.txt`:

```
cmake_minimum_required(VERSION 3.27)

project(example LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
```

Depending on how you installed MLX, you may need to tell CMake where to
find it.

If you installed MLX with Python, then add the following to the CMake file:

```
find_package(
  Python 3.9
  COMPONENTS Interpreter Development.Module
  REQUIRED)
execute_process(
  COMMAND "${Python_EXECUTABLE}" -m mlx --cmake-dir
  OUTPUT_STRIP_TRAILING_WHITESPACE
  OUTPUT_VARIABLE MLX_ROOT)
```

If you installed the MLX C++ package to a system path, then CMake should be
able to find it. If you installed it to a non-standard location or CMake can’t
find MLX then set `MLX_ROOT` to the location where MLX is installed:

```
set(MLX_ROOT "/path/to/mlx/")
```

Next, instruct CMake to find MLX:

```
find_package(MLX CONFIG REQUIRED)
```

Finally, add the `example.cpp` program as an executable and link MLX.

```
add_executable(example example.cpp)
target_link_libraries(example PRIVATE mlx)
```

You can build the example with:

```
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build
```

And run it with:

```
./build/example
```

Note `find_package(MLX CONFIG REQUIRED)` sets the following variables:

| Variable | Description |
| --- | --- |
| MLX_FOUND | Trueif MLX is found |
| MLX_INCLUDE_DIRS | Include directory |
| MLX_LIBRARIES | Libraries to link against |
| MLX_CXX_FLAGS | Additional compiler flags |
| MLX_BUILD_ACCELERATE | Trueif MLX was built with Accelerate |
| MLX_BUILD_METAL | Trueif MLX was built with Metal |
