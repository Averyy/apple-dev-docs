# Matrices and Vectors

**Framework**: Metal Performance Shaders

Solve systems of equations, factorize matrices and multiply matrices and vectors.

## Topics

### Matrices
- [class MPSMatrix](mpsmatrix.md)
  A 2D array of data that stores the data’s values.
- [class MPSMatrixDescriptor](mpsmatrixdescriptor.md)
  A description of attributes used to create an MPS matrix.
- [class MPSTemporaryMatrix](mpstemporarymatrix.md)
  A matrix allocated on GPU private memory.
### Vectors
- [class MPSVector](mpsvector.md)
  A 1D array of data that stores the data’s values.
- [class MPSVectorDescriptor](mpsvectordescriptor.md)
  A description of the length and data type of a vector.
- [class MPSTemporaryVector](mpstemporaryvector.md)
  A vector allocated on GPU private memory.
### Classes for Decomposition and Solving
- [class MPSMatrixDecompositionCholesky](mpsmatrixdecompositioncholesky.md)
  A kernel for computing the Cholesky factorization of a matrix.
- [class MPSMatrixSolveCholesky](mpsmatrixsolvecholesky.md)
  A kernel for computing the solution of a linear system of equations using a Cholesky factorization.
- [class MPSMatrixDecompositionLU](mpsmatrixdecompositionlu.md)
  A kernel for computing the LU factorization of a matrix using partial pivoting with row interchanges.
- [class MPSMatrixSolveLU](mpsmatrixsolvelu.md)
  A kernel for computing the solution of a linear system of equations using an LU factorization.
- [class MPSMatrixSolveTriangular](mpsmatrixsolvetriangular.md)
  A kernel for computing the solution of a linear system of equations using a triangular coefficient matrix.
- [class MPSMatrixUnaryKernel](mpsmatrixunarykernel.md)
  A kernel that consumes one matrix and produces one matrix.
- [class MPSMatrixBinaryKernel](mpsmatrixbinarykernel.md)
  A kernel that consumes two matrices and produces one matrix.
- [enum MPSMatrixDecompositionStatus](mpsmatrixdecompositionstatus.md)
### Matrix Arithmetic Operations
- [class MPSMatrixSum](mpsmatrixsum.md)
  A kernel for performing a pointwise summation of a matrix.
- [class MPSMatrixMultiplication](mpsmatrixmultiplication.md)
  A matrix multiplication kernel.
- [class MPSMatrixVectorMultiplication](mpsmatrixvectormultiplication.md)
  A matrix-vector multiplication kernel
- [class MPSMatrixFindTopK](mpsmatrixfindtopk.md)
  A kernel for computing the top-K values and their corresponding indices in a matrix.
### Matrix Copying Operations
- [class MPSMatrixCopy](mpsmatrixcopy.md)
  A class that can perform multiple matrix copy operations.
- [class MPSMatrixCopyToImage](mpsmatrixcopytoimage.md)
  A kernel that copies matrix data to a Metal Performance Shaders image.
- [class MPSMatrixCopyDescriptor](mpsmatrixcopydescriptor.md)
  A description of multiple matrix copy operations.
- [class MPSImageCopyToMatrix](mpsimagecopytomatrix.md)
  A class that copies image data to a matrix.
### Matrix Neural Network Operations
- [class MPSMatrixFullyConnected](mpsmatrixfullyconnected.md)
  A kernel for applying a fully connected neural network layer.
- [class MPSMatrixFullyConnectedGradient](mpsmatrixfullyconnectedgradient.md)
  A kernel for applying a fully gradient connected neural network layer.
- [class MPSMatrixNeuron](mpsmatrixneuron.md)
  A neuron activation kernel that operates on matrices.
- [class MPSMatrixNeuronGradient](mpsmatrixneurongradient.md)
  A gradient neuron activation kernel that operates on matrices.
### Matrix Softmax Operations
- [class MPSMatrixLogSoftMax](mpsmatrixlogsoftmax.md)
  A logarithmic softmax kernel that operates on matrices.
- [class MPSMatrixLogSoftMaxGradient](mpsmatrixlogsoftmaxgradient.md)
  A logarithmic gradient softmax kernel that operates on matrices.
- [class MPSMatrixSoftMax](mpsmatrixsoftmax.md)
  A softmax kernel that operates on matrices.
- [class MPSMatrixSoftMaxGradient](mpsmatrixsoftmaxgradient.md)
  A gradient softmax kernel that operates on matrices.
### Matrix Normalization Operations
- [class MPSMatrixBatchNormalization](mpsmatrixbatchnormalization.md)
  A batch normalization kernel that operates on matrices.
- [class MPSMatrixBatchNormalizationGradient](mpsmatrixbatchnormalizationgradient.md)
  A batch normalization gradient kernel that operates on matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/matrices-and-vectors)*